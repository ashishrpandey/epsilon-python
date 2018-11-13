#!/bin/python3


myfileObj = open("studentrecord.txt", "r") # r, w , a 
mylocFile = open("location.txt", "w")
content = myfileObj.readline()
for line in content:
	print(line, myfileObj.tell())
	
	#if(line.lower().find("karle")!= -1):
	#	print ("Got the string Alert!!" )
	#	print(line)
	#record = line.split(",")
	#print(record[1])
	#mylocFile.write(record[1] + "\n")
	#print(record[2])
mylocFile.close()
myfileObj.close()
