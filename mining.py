#!/usr/bin/python
import os
import time
import datetime
from subprocess import call

def killMining():
	file = open("C:\\Users\\Jay\\Dropbox\\mine.txt","r")
	continueMining = file.read(10)
	print (continueMining)
	file.close()
	
	time = datetime.datetime.now().hour
	print(time)
	
	if "no" in continueMining:
		return True
	elif "shutdown" in continueMining:
		shutdown()
	elif "lite" in continueMining:
		liteCoinMining()
	elif "doge" in continueMining:
		dogeCoinMining()
	elif "feather" in continueMining:
		featherCoinMining()
	elif time == 3:
		shutdown()
	else:
		return False
		
def liteCoinMining():
	#C:\\cudaminer-2013-12-18\\x64\\cudaminer.exe -l auto -H 1 -i 0 -C 1 -D -o stratum+tcp://stratum-eu.doge.luckyminers.com:3313 -O hacker9116.1:1
	os.system("	C:\\cudaminer-2013-12-18\\x64\\cudaminer.exe -l auto -H 1 -i 0 -C 1 -D -o stratum+tcp://coinotron.com:3334 -O jaslloyd.1:1")


def dogeCoinMining():
	os.system("C:\\cudaminer-2013-12-18\\x64\\cudaminer.exe -l auto -H 1 -i 0 -C 1 -D -o stratum+tcp://teamdoge.com:3333 -O hacker9116.1:1")

def featherCoinMining():
	os.system("C:\\cudaminer-2013-12-18\\x64\\cudaminer.exe -l auto -H 1 -i 0 -C 1 -D -o stratum+tcp://stratum.wemineftc.com:3333 -O hacker9116.1:1")

def shutdown():
	os.system("shutdown -s")
	
if killMining():
	os.system("TASKKILL /F /IM cudaminer.exe")
	
else:
	#os.system("copy /Y C:\Users\Jay\miner.log C:\Users\Jay\Dropbox")
	print ("Task not open no need to run")