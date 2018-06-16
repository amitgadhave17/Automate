#This is logger application which log the daily count of SML and SMTS count of detections and samples.
#Author -	Amit Gadhave
#Date 	- 	13/06/2018

import csv
import sys, os, time
from datetime import datetime

def getDayMonth():
	tday = datetime.today().day
	tmon = datetime.today().strftime("%B")
	return tday, tmon

def insertRecord():
	try:
		with open("Database/" + tmon + ".csv", "wb") as CSVfile:
			CSVReader = csv.reader(CSVfile, delimiter = ',')
	except:
		print ("something is not right=")


if __name__=="__main__":
	line1 = input("Sample_Count | a-SML/b-SMTS/c-Something_else | Description\n")
	print(line1)
	listline = line1.split(" ")
	p
	try:
		sampleCount = int(listline[0])
		detType = "OTHER"
		if listline[1] == 'a' or listline[1] == 'A':
			detectionType = "SML"
		elif listline[1] == 'B' or listline[1] == 'B':
			detectionType = "SMTS"
		desc = " ".join(listline[1:])
		print sampleCount
		print detType
		print desc
	except:
		print("Wrong Input")

	if len(sys.argv) == 2:
		print(sys.argv[1])
	else:
		# inserting record today
		print(line)