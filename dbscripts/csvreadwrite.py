import csv 

myreader = csv.reader(open("studentrecord.txt","r"))
print(list(myreader)[2][3])
