#Thanks to http://www.instructables.com/id/Plotting-real-time-data-from-Arduino-using-Python-/
import sys, serial, argparse
import numpy as np
from time import sleep
from collections import deque
import json
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import datetime  
import time

class AnalogPlot:
	def __init__(self, serialPort, channel, logging, maxLengh):
		self.ser = serial.Serial(serialPort, 9600)
		self.ax = deque([0.0]*maxLengh)
		self.ay = deque([0.0]*maxLengh)
		self.maxLen = maxLengh
		self.channel = channel
		self.logging = logging
		if (logging):
			now = datetime.datetime.now()
			timestamp = int(time.mktime(now.timetuple()))
			self.file_object = open("raw_"+channel+"_"+str(timestamp)+".csv", "w")
	
	def addToBuf(self, buf, val):
		if len(buf) < self.maxLen:
			buf.append(val)
		else:
			buf.pop()
			buf.appendleft(val)

	def add(self, data):
		print data
		self.addToBuf(self.ax, data['time'])
		self.addToBuf(self.ay, data['value'])

	def update(self, frameNum, a0, a1):
		try:
			message = self.ser.readline()
			
			line = json.loads(message)
          	# print data
			if(line['channel'] == self.channel):
				if(self.logging):
					self.file_object.write(str(line['value']) + "," + str(line['time']) + "\n")
				self.add(line)
				a0.set_data(self.ax, self.ay)
		except KeyboardInterrupt:
			print('exiting')
		return a0, 

  	def close(self):
    	# close serial
		self.ser.flush()
		self.ser.close()    

def main():
	parser = argparse.ArgumentParser(description="Digital/Analogic oscilloscope")
	parser.add_argument('--port', dest='port', required=True, help="Serial port to use")
	parser.add_argument('--channel', dest='channel', required=True, help='choose which channel to draw in [channel_1, channel_2, channel_3, channel_a, channel_v]')
	parser.add_argument("--log", dest="log", required=False, type=bool, default=False, help='log raw data into a file')
	args = parser.parse_args()
	serialPort = args.port
	channel = args.channel
	logging = args.log

	analogPlotter = AnalogPlot(serialPort,channel, logging, 5000)

	fig = plt.figure()
	if(channel == "channel_a"):
		ax = plt.axes(xlim=(0,2000), ylim=(0,1023))
	elif(channel == "channel_v"):
		ax = plt.axes(xlim=(0,5000), ylim=(0,5100))
	else:
		ax = plt.axes(xlim=(0,2000), ylim=(0,1))
	a0, = ax.plot([], [])
  	a1, = ax.plot([], [])
  	anim = animation.FuncAnimation(fig, analogPlotter.update, fargs=(a0,a1), interval=50)

  	# show plot
  	plt.show()
  
  	# clean up
  	analogPlot.close()

# call main
if __name__ == '__main__':
  main()
