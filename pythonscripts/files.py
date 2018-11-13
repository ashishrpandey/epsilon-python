#!/bin/python3

'''
myfileObj = open("myfile.txt", "a") # r, w , a 
l = [1,2,3,4]

s = "Ashish"
myfileObj.write(s)
myfileObj.write("Adding some more things in file \n")
myfileObj.write(str(l))


for i in range(5):
	myfileObj.write(" My line number is " + str(myfileObj.tell()) + "\n")

'''
myfileObj = open("myfile.txt", "r") # r, w , a 

#content = myfileObj.read()
#print(content)
lines = myfileObj.readlines()
print(lines)
#print(line1, str(myfileObj.tell()))
myfileObj.close()

#myfileObj.tell()
#print(help(myfileObj.read))
#for i in content:
#	print(i)

#print( myfileObj.tell())
#
#line2 = myfileObj.readline()
#print(line2)
#print( myfileObj.tell())
#
#line3 = myfileObj.readline()
#print(line3)
#print( myfileObj.tell())
#myfileObj.close()
