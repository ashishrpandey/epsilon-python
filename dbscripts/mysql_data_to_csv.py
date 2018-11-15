#!/usr/bin/python

import MySQLdb
import csv
# Open database connection
db = MySQLdb.connect("zekeserver.ctxzguosahx8.ap-south-1.rds.amazonaws.com","user","zeketraining","zekedb" )
print(dir(csv))

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM EMPLOYEE"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   writer = csv.writer(open("outfile.csv", 'w'))
   for row in results:
      writer.writerow(row)       
except:
   print "Error: unable to fecth data"

db.close()

