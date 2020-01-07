WIFI_SSID = 'YOUR_WIFI_SSID'
WIFI_PWD = 'YOUR_WIFI_PASSWORD'

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(WIFI_SSID, WIFI_PWD)
        while not wlan.isconnected():
            pass
    print('network config: ', wlan.ifconfig())

do_connect()