myfileObj = open("studentrecord.txt", "r") # r, w , a

line1 = myfileObj.readline()
print(line1)
print (myfileObj.tell())

myfileObj.seek(15)
content = myfileObj.readlines()
len(content)
print(line2)
print (myfileObj.tell())

line3 = myfileObj.readline()
print(line3)
print (myfileObj.tell())
