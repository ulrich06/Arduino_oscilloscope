import sys, serial, argparse
import numpy as np
from time import sleep
from collections import deque
import json
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
class AnalogPlot:
	def __init__(self, serialPort, channel, maxLengh):
		self.ser = serial.Serial(serialPort, 9600)
		self.ax = deque([0.0]*maxLengh)
		self.ay = deque([0.0]*maxLengh)
		self.maxLen = maxLengh
		self.channel = channel

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
				self.add(line)
		#		a0.set_data(range(self.maxLen), self.ax)
				a0.set_data(self.ax, self.ay)
		except KeyboardInterrupt:
			print('exiting')
		return a0, 

  	def close(self):
    	# close serial
		self.ser.flush()
		self.ser.close()    

def main():
	parser = argparse.ArgumentParser(description="LDR serial")
	parser.add_argument('--port', dest='port', required=True)
	parser.add_argument('--channel', dest='channel', required=True)

	args = parser.parse_args()
	serialPort = args.port
	channel = args.channel

	print(channel)

	analogPlotter = AnalogPlot(serialPort,channel,5000)

	fig = plt.figure()
	if(channel == "channel_a"):
		ax = plt.axes(xlim=(0,2000), ylim=(0,1023))
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
