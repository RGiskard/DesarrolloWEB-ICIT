import os
import subprocess
import re
from unicodedata import normalize
class DeviceHandler:
	def __init__(self,version):
		self.__comandsBaseLeft={\
		6:"adb shell service call isms 7 i32 1 s16 \"com.android.mms\" s16 \"",\
		7:"adb shell service call isms 7 i32 1 s16 \"com.android.mms\" s16 \"",\
		8:"adb shell service call isms 7 i32 0 s16 \"com.android.mms.service\" s16 \"",\
		#9:"adb shell service call isms 7 i32 1 s16 \"com.android.mms\" s16 \""}
		9:"adb shell service call isms 7 i32 0 s16 \"com.android.mms.service\" s16 \""}
		self.__comandsBaseRight={\
		6:"\" s16 \"null\" s16 \"null\"",\
		7:"\" s16 \"null\" s16 \"null\"",\
		8:"\" s16 \"null\" s16 \"null\"",\
		#9:"\" s16 \"null\" s16 \"null\""}
		9:"\" s16 \"null\" s16 \"null\""}
		self.__comandsBasemiddle={\
		6:"\" s16 \"null\" s16 \"",\
		7:"\" s16 \"null\" s16 \"",\
		8:"\" s16 \"null\" s16 \"",\
		#9:"\" s16 \"null\" s16 \""}
		9:"\" s16 \"null\" s16 \""}
		self.__androidVersion=version;
		if version.find('.')>0:
			self.__versionkey=int(version[0:version.find('.')])
		else:
			self.__versionkey=int(version)
	def sendSMS(self,number,body):
		comand=self.__comandsBaseLeft[self.__versionkey]+number+self.__comandsBasemiddle[self.__versionkey]\
		+body+self.__comandsBaseRight[self.__versionkey]
		#DETACHED_PROCESS = 0x00000008
		#subprocess.call(comand, creationflags=DETACHED_PROCESS)
		#print(comand)
		os.system(comand)

	def makeCall(self,number):
		comand = "adb shell am start -a android.intent.action.CALL -d tel:"+number
		os.system(comand)

	def endCall(self):
		comand = "adb shell input keyevent 6"
		os.system(comand)

	def __str__(self):
		return "DeviceHandler android version "+str(self.__androidVersion)

	@staticmethod
	def prepareNumber(number):
		if '.' in number:
			index=number.index('.')
			number=number[:index]
			return number
		else:
			return number	

	@staticmethod
	def prepareSMS(smsbody):
		smsPrepared=smsbody.replace(' ','\ ')
		specialCharDic={'.':'\.','(':'\(',')':'\)','-':'\-'}
		specialChar=specialCharDic.keys()
		for ch in specialChar:
			smsPrepared=smsPrepared.replace(ch,specialCharDic[ch])
		smsPrepared=re.sub(
		r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
		normalize( "NFD", smsPrepared), 0, re.I
		)
		smsPrepared = normalize( 'NFC', smsPrepared)
		return smsPrepared

#pyinstaller --onefile --icon=app.ico --clean --noconsole app.py

