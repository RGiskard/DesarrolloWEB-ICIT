import os
import time
class Connector:
	def __init__(self):
		self.__Init=False
		self.__Comands={'init':"adb start-server",'devices':"adb devices",'kill':"adb kill-server",'key':"device"}
	def beginDevice(self):
		os.system(self.__Comands['init'])
	def ready(self):
		valCmd=os.popen(self.__Comands['devices']).read().count(self.__Comands['key'])
		if valCmd==2:
			self.__Init=True
		return self.__Init
	def androidVersion(self):
		version=os.popen("adb shell getprop ro.build.version.release").read()
		version=version.replace('\n', '')
		return version
	def closeDevice(self):
		os.system(self.__Comands['kill'])	
	def launch(self):
		self.beginDevice()
