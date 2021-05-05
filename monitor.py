#!/bin/python
# This file is part of CRM.

# CRM is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# CRM is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along with CRM. If not, see
# <https://www.gnu.org/licenses/>.
import psutil, os, time, termcolor, config

class Formater:
	def createBar(current : float):
		bar = '[';
		for i in range(100):
			if i < current:
				bar += termcolor.colored(config.bar["char"],config.bar["usedColor"])
			else:
				bar += termcolor.colored(config.bar["char"],config.bar["freeColor"])
		bar += "]" + str(current) + "%"
		return bar
	def boldText(printed : str):
		return "\033[1m" + printed + "\033[0m"
	
	def centerText(parameterString : str):
		rows, columns = os.popen('stty size', 'r').read().split()
		return parameterString.center(int(columns), config.fillChar)
	
	def boldCentered(printed : str):
		return Formater.boldText(Formater.centerText(printed))

class CPU:
	def __init__(self):
		self.frequency = None
		self.percentage = None
		self.processes = None
	def update(self):
		self.frequency = round(psutil.cpu_freq()[0]/1000,2)
		self.percentage = psutil.cpu_percent()
		self.processes = len(psutil.pids())
	def printData(self):
		data = Formater.boldCentered("CPU") if config.titles else ""
		data += str(self.frequency) + " Ghz\n"
		if config.CPU_BAR:
			data += Formater.createBar(self.percentage)
		data += "\n" + str(self.processes) + " Processes\n"
		return data

class Memory:
	def __init__(self):
		self.total = None
		self.used = None
		self.percentage = None
	def update(self):
		GB = 1024 ** 3
		mem = psutil.virtual_memory()
		self.total = mem[0]/GB
		self.percentage = mem[2]
		self.used = mem[3]/GB
	def printData(self):
		data = Formater.boldCentered("Memory") if config.titles else ""
		data += str(round(self.used,2))+'GB/'+str(round(self.total,2)) + "GB\n"
		if(config.MEM_BAR):
			data += Formater.createBar(self.percentage)
		return data

class Temperature:
	def __init__(self):
		self.max = None
		self.current = None
	def update(self):
		temp = psutil.sensors_temperatures()["acpitz"][0]
		self.max = temp[3]
		self.current = temp[1]
	def printData(self):
		data = ""
		if config.titles:
			data = '\n' + Formater.boldCentered("Temperature") + "\n"
		#print(str(self.current)+"°C/"+str(self.max) + "°C")
		data += str(self.current) + "°C/" + str(self.max) + "°C\n"
		if(config.TEMP_BAR):
			data += Formater.createBar(self.current*100/self.max)
		return data

class Monitor:
	def __init__(self):
		self.cpu = CPU()
		self.mem = Memory()
		self.temp = Temperature()
	def update(self):
		self.cpu.update()
		self.mem.update()
		self.temp.update()
	def printData(self):
		os.system("clear");
		str = ""
		if(config.CPU_INFO):
			str += self.cpu.printData()
		if(config.MEM_INFO):
			str += self.mem.printData()
		if(config.TEMP_INFO):
			str += self.temp.printData()
		print(str)
		time.sleep(config.updateInterval)
	def loop(self):
		try:
			while True:
				self.update()
				self.printData()
		except KeyboardInterrupt:
			print(" Goodbye!")
def main():
	monitor = Monitor()
	monitor.loop()
if __name__ == '__main__':
	main()