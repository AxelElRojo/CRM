#/bin/python
import psutil, os, time, termcolor, config
class printer:
	def printBar(current : float):
		print('[',end="")
		for i in range (100):
			if i < current:
				print(termcolor.colored(config.bar["char"],config.bar["usedColor"]),end="")
			else:
				print(termcolor.colored(config.bar["char"],config.bar["freeColor"]),end="")
		print("] " + str(current) + "%")
	def printBold(printed : str):
		print("\033[1m" + printed + "\033[0m")
	def centerText(string : str):
		rows, columns = os.popen('stty size', 'r').read().split()
		return string.center(int(columns),config.fillChar)
	def printBoldCentered(printed : str):
		printer.printBold(printer.centerText(printed))

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
		if config.titles:
			printer.printBoldCentered("CPU")
		print(str(self.frequency) + " Ghz")
		if(config.CPU_BAR):
			printer.printBar(self.percentage)
		print(str(self.processes) + " Processes")

class Memory:
	def __init__(self):
		self.total = None
		self.used = None
		self.percentage = None
	def update(self):
		GB = 1000 ** 3
		mem = psutil.virtual_memory()
		self.total = mem[0]/GB
		self.percentage = mem[2]
		self.used = mem[3]/GB
	def printData(self):
		if config.titles:
			printer.printBoldCentered("Memory")
		print(str(round(self.used,2))+'GB/'+str(round(self.total,2))+'GB')
		if(config.MEM_BAR):
			printer.printBar(self.percentage)

class Temperature:
	def __init__(self):
		self.max = None
		self.current = None
	def update(self):
		temp = psutil.sensors_temperatures()["acpitz"][0]
		self.max = temp[3]
		self.current = temp[1]
	def printData(self):
		if config.titles:
			print()
			printer.printBoldCentered("Temperature")
		print(str(self.current)+"°C/"+str(self.max) + "°C")
		if(config.TEMP_BAR):
			printer.printBar(self.current*100/self.max)

class Monitor:
	def __init__(self):
		self.cpu = CPU()
		self.mem = Memory()
		self.temp = Temperature()
	def update(self):
		self.cpu.update()
		self.mem.update()
		self.temp.update()
		time.sleep(config.updateInterval)
	def printData(self):
		time.sleep(config.updateInterval)
		os.system("clear");
		if(config.CPU_INFO):
			self.cpu.printData()
		if(config.MEM_INFO):
			self.mem.printData()
		if(config.TEMP_INFO):
			self.temp.printData()
	def loop(self):
		try:
			while True:
				self.update()
				self.printData()
		except KeyboardInterrupt:
			pass
def main():
	monitor = Monitor()
	monitor.loop()
if __name__ == '__main__':
	main()