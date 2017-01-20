Arduino Oscilloscope
=====================

This is a simple implementation of an oscilloscope based on Arduino. It samples digital or analogic data, send them through the serial port (JSON format) and display them on your monitor.

## Arduino platform

The arduino platform provides 3 digital channels (1,2,3) and an analogic channel (a). Several constants are defined:

* LED_GREEN, LED_RED, LED_BLUE, LED_A are respectively the led assocated to the channels 1, 2, 3 and A
* CHANNEL_1, CHANNEL_2, CHANNEL_3, CHANNEL_A are respectively the pin associated to the channel inputs
* DELAY defines (in ms) the sampling rate (default=200ms)


## Python code

The python code has been inspired from the project [Plotting Real Time data from Arduino using Python](http://www.instructables.com/id/Plotting-real-time-data-from-Arduino-using-Python-/).

Usage:

''' python oscilloscope.py --port SERIAL_PORT --channel CHANNEL [--log [True|False] ] '''

where

* --port SERIAL_PORT is the serial port on which the Arduino is connected
* --channel CHANNEL is the oscilloscope channel (any value in {channel_1, channel_2, channel_3, channel_a)
* --log True|False logs the data into a csv file located in the working directory (optional argument)