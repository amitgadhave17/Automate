#|-----------------------------------------------------------------------------------------------------
#|This is logger application which log the daily count of SML and SMTS count of detections and samples.
#|Author -	Amit Gadhave
#|Date 	- 	13/06/2018
#|-----------------------------------------------------------------------------------------------------

import csv, calendar
import sys, os, time
from datetime import datetime

def getDayMonth():
	tday = datetime.today().day
	tmon  = calendar.month_abbr[datetime.today().month]
	return tday, tmon

def getRecord(tdate):
	if len(tdate) < 2:
		return False
	tday = tdate[0]
	tmon = tdate[1]
	sampleCount = 0
	monthSampleCount = 0

	try:
		CSVfile = open("Database/" + tmon + ".csv", "r")
		CSVReader = csv.reader(CSVfile, delimiter = ',')

		# Read all records
		for row in CSVReader:
			# if inserting date found in readed data,update day count
			if tday == int(row[0]):
				sampleCount = int(row[1])
			monthSampleCount = monthSampleCount + int(row[1])
	except:
		print("File read  fails")

	# prining sample count for day and month
	print(str(tday) + "-" + tmon + ": " + str(sampleCount))
	print(tmon + ": " + str(monthSampleCount))
	return True

if __name__=="__main__":
	try:
		#Get todays day and month
		tdate = getDayMonth()

		if len(sys.argv) == 2:
			#Get user input day and month
			listline = sys.argv[1].split("-")
			tday = int(listline[0])
			tmon = ""
			try:
				tmon = calendar.month_abbr[int(listline[1])]
			except:
				tmon  = listline[1]
			tdate = (tday, tmon)

		bret = getRecord(tdate)
	except:
		print("Wrong Input")
