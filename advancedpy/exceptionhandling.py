#exceptions:
a = [1]
b = "ashish"
try :
	assert( b == "Ashish")
	#if (b != "Ashish"):
	#	raise ValueError;

#except NameError:
#	print('this is a name error')

except ValueError:
	print ('this is a value error')

except IndexError:
	print ('this is an index  error')
except :
	print ('this is a generic error')

else:
	print ('this is else block : There is no error')

finally:
	print ('this is finally: will be printed everytime')
#assertion
'''
def func(a,b):
	assert b != 0
	print(a/b)
#	print (a)

func(2,1)
# creating your own exception

class myException(RuntimeError):
	def __init__(self, arg):
		self.arg=arg

#raise myException('hi')

try:
	a=6
	if (a==6):
		#b=input("enter")
		#b= 5 
		raise myException(a)
except myException as e :
	print("raised an exception with value = ", e.arg)

'''
