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

def insertRecord(tdate, data):
	if len(tdate) < 2:
		return False
	tday = tdate[0]
	tmon = tdate[1]
	sampleCount = data[0]
	detType = data[1]
	desc = data[2]

	data = []
	bFind = False
	monthSampleCount = 0

	try:
		CSVfile = open("Database/" + tmon + ".csv", "r")
		CSVReader = csv.reader(CSVfile, delimiter = ',')

		# Read all records
		for row in CSVReader:
			# if inserting date found in readed data,update day count
			if tday == int(row[0]):
				row[1] = int(row[1]) + sampleCount
				sampleCount = row[1]
				row.append(detType + "|" + str(sampleCount) + "|" + desc)
				bFind = True
			monthSampleCount = monthSampleCount + int(row[1])
			data.append(row)
	except:
		print ("File read  fails")

	# if days first record going to be inserted
	if bFind is False:
		monthSampleCount = monthSampleCount + sampleCount
		row = [tday,sampleCount, detType + "|" + str(sampleCount) + "|" + desc]
		data.append(row)

	# Writing all records(Updated)
	try:	
		CSVfile = open("Database/" + tmon + ".csv", "wb")
		CSVWriter = csv.writer(CSVfile, delimiter = ',')
		for row in data:
			CSVWriter.writerow(row)
	except:
		print("File Creation Fails")

	data = []
	bFind = False

	# Getting sample count from Year File
	try:	
		CSVfile = open("Database/Info.csv", "r")
		# Read all month records
		for row in CSVReader:
			# if inserting date found in readed data,update day count
			if tmon == row[0]:
				row[1] = monthSampleCount
				bFind = True
			data.append(row)
	except:
		print("File read Fails")

	#if months first record going to be inserted
	if bFind is False:
		row = [tmon, monthSampleCount]
		data.append(row)

	# Writing all records(Updated) 
	try:
		CSVfile = open("Database/Info.csv", "wb")
		CSVWriter = csv.writer(CSVfile, delimiter = ',')
		for row in data:
			CSVWriter.writerow(row)
	except:
		print("File Creation Fails")
	
	# prining sample count for day and month
	print(str(tday) + "-" + tmon + ": " + str(sampleCount))
	print(tmon + ": " + str(monthSampleCount))
	return True

if __name__=="__main__":
	line1 = raw_input("Sample_Count | a-SML/b-SMTS/c-Something_else | Description\n")
	listline = line1.split(" ")
	try:
		sampleCount = int(listline[0])
		detType = "OTHER"
		if str(listline[1]) == "a":
			detType = "SML"
		else:
			detType = "SMTS"
		desc = " ".join(listline[2:])

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

		bret = insertRecord(tdate, (sampleCount, detType, desc))
	except:
		print("Wrong Input")

		