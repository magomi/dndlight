# Summary

A quick and dirty implementation of a DoNotDisturb light using micropython on an ESP8266. 

The controller hosts a small webserver that serves a page that has controls to switch the color of a light between red and blue.
The light is simply a strip of RGB LED (WS2812/Neopixel).

# Installation

* install micropyhton on your device
* change boot.py according to your local wifi settings
* change main.py according to the physical wiring of your device
  * PIXEL_CNT: number of neopixels you want to control
  * PIN_NUMBER: number of the GPIO port where the pixel bus is connected
* upload boot.py and main.py to the device

# Useage

* get the IP address of the device within your local wifi
  * check the log of your access point or 
  * connect to the serial console of the device and reboot, the network settings will be printed
* open [http://IP_ADDRESS/](http://IP_ADDRESS/) in your browser and click the buttons for the color settings
* you can also call [http://IP_ADDRESS/?dnd=GREEN](http://IP_ADDRESS/?dnd=GREEN) or [http://IP_ADDRESS/?dnd=RED](http://IP_ADDRESS/?dnd=RED) directly
  * only setting of red or green is implemented, if any other COLOR will be send the device switches to 
    an very dark white
* on startup the the color is set to a very dark white

# Resources

* [micropython](http://docs.micropython.org/en/latest/index.html)
  * [esp8266](http://docs.micropython.org/en/latest/esp8266/quickref.html)
    * [connect wifi](http://docs.micropython.org/en/latest/esp8266/quickref.html#networking)
    * [neopixel](http://docs.micropython.org/en/latest/esp8266/quickref.html#neopixel-driver)    
* [webserver on micropython](https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/)
* [micropython on intellij idea](https://plugins.jetbrains.com/plugin/9777-micropython)
