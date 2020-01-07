# Summary

A quick and dirty implementation of a DoNotDisturb light using micropython on an ESP8266. 

The controller hosts a small webserver that serves a page that has controls to switch a light on and off.
The light is simply a RGB LED (WS2812/Neopixel).

# Installation

* install micropyhton on our device
* change boot.py according to your local wifi settings
* change main.py according to the physical wiring of your device
  * PIXEL_CNT: number of neopixels you want to control
  * PIN_NUMBER: number of the GPIO port where the pixel bus is connected
* upload boot.py and main.py to the device

# Useage

* get the IP address of the device within your local wifi
  * check the log of your access point or 
  * connect to the serial console of the device and reboot, the network settings will be printed
* open [http://<ip-address>/](http://<ip-address>/) in your browser and click the buttons for the color settings
* you can also call [http://<ip-address>/?dnd=GREEN](http://<ip-address>/?dnd=GREEN) or [http://<ip-address>/?dnd=RED](http://<ip-address>/?dnd=RED) directly
  * only setting of red or green is implemented, if any other COLOR will be send the device switches to 
    an very dark white
* on startup the the color is set to a very dark white

# Resources

* [micropython](http://docs.micropython.org/en/latest/index.html)
  * [esp8266](http://docs.micropython.org/en/latest/esp8266/quickref.html)
    * [connect wifi](http://docs.micropython.org/en/latest/esp8266/quickref.html#networking)
    * [neopixel](http://docs.micropython.org/en/latest/esp8266/quickref.html#neopixel-driver)
    
* [webserver on micropython](https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/)
