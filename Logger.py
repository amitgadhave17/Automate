#This is logger application which log the daily count of SML and SMTS count of detections and samples.
#Author -	Amit Gadhave
#Date 	- 	13/06/2018

import csv
import sys, os, time
from datetime import datetime

tday = datetime.today().day
tmon = datetime.today().strftime("%B")

try:
	with open("Database\\" + tmon + ".csv", "wb") as CSVfile:
		pass
except:
	print "something is not right="