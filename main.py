from machine import Pin
from neopixel import NeoPixel
import usocket as socket

PIXEL_CNT = 5
PIN_NUMBER = 5

np_pin = Pin(PIN_NUMBER)
np = NeoPixel(np_pin, PIXEL_CNT, bpp=4)

def web_page():
    html = """
    <html>
      <head>
        <title>Do Not Disturb</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="data:,">
        <style>
          html {
            font-family: sans-serif; 
            display:inline-block; 
            margin: 0px auto; 
            text-align: center;
          }
          h1 {
            color: #000000; 
            padding: 2vh;
          }
          p {
            font-size: 1.5rem;
          }
          .button {
            display: inline-block; 
            background-color: #555555; 
            border: none; 
            border-radius: 10px; 
            color: white; 
            padding: 16px 40px; 
            text-decoration: none; 
            font-size: 30px; 
            margin: 2px; 
            cursor: pointer;
          }
          .red {
            background-color: #ff0000;
            width: 200px;
          }
          .green {
            background-color: #00ff00;
            width: 200px;
          }
        </style>
      </head>
      <body> 
        <h1>Do Not Disturb</h1>
        <p><a href="/?dnd=G"><button class="button green">GREEN</button></a></p>
        <p><a href="/?dnd=R"><button class="button red">RED</button></a></p>
      </body>
    </html>
    """
    return html

def set_color(color):
    for i in range(0, PIXEL_CNT):
        np[i] = color
    np.write()

def set_red():
    set_color((255, 0, 0, 0))

def set_yellow():
    set_color((255, 255, 0, 0))
    
def set_green():
    set_color((0, 255, 0, 0))

def set_lightwhite():
    set_color((0, 0, 0, 1))

set_lightwhite()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('CONNECTION from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('REQUEST CONTENT = %s' % request)
    request_query = request.split(' ')[1]
    print('REQUEST QUERY = %s' % request_query)
    if (request_query.startswith('/?dnd=')):
        request_color = request_query.split('=')[1]
        if (request_color == 'G'):
            set_green()
        elif (request_color == 'R'):
            set_red()
        elif (request_color == 'B'):
            set_blue()
        elif (request_color == 'Y'):
            set_yellow()
        else:
            set_lightwhite()

    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Length: ')
    conn.send(str(len(response)))
    conn.send('\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
