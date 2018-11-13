#!/bin/python3
'''
def add(arg1,arg2,arg3):
	sum = arg1 + arg2 +arg3 
	return sum

#
arg1 = 1
arg2 = 2
arg3 = 3
result = add(arg1,arg2)
print(result)

#default positional argument
'''
def function(arg1 = "deafult arg1 ",arg2 = "default arg2", arg3 = "default argument 3" ):
    print("************************")
    print(arg1)
    print(arg2)
    print(arg3)

a= "my argument 1"
b= "my argument 2"
c = "my argument 3"
function(a,c,b)
#function()
#function(arg2 = b, arg1 =a )


#function(arg3 = "keword argument")
#function("only argument ", "2nd argument")

