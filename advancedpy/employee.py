class employee():
	def __init__(self,name_arg = "None",empid_arg = 0):
		self.name = name_arg
		self.empid= empid_arg
		self.designation = "engineer"
		pass
	def __str__(self):
		return (self.name + " , " + str(self.empid) + " , " + self.designation)

	def promote(self, designation_arg):
		self.designation = designation_arg
'''
a = employee("Nagesh",23)
b = employee()
print(a)
print(b)
'''



a = employee()
b = employee("Nagesh1")
c = employee("Nagesh2")
d = employee("Nagesh3")
e = employee("Nagesh4")
#
print(a.name,a.empid)
a.name = "Ashish"
a.empid = 11222
print(a)
a.promote("President")
print(a)
#print(dir(a))
print(a.__dict__)

#print(b.name)
#print(c.name)
#print(d.name)
#print(e.name)
