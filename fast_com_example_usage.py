#!/usr/bin/env python

import fast_com
import schedule
import time
import datetime

def job():
	speed = fast_com.fast_com()
	print "Result:", speed, "Mbps"
	st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	with open("speeds.log", "a") as logFile:
		logFile.write(st +","+str(speed))
		logFile.close()

schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)