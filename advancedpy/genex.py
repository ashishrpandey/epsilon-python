def myGenerator():
       i=0
       while i<5:
               yield i
               i+=1
f=myGenerator()
print (next(f))
print (next(f))
print (next(f))
print (next(f))
print (next(f))
print (next(f))

