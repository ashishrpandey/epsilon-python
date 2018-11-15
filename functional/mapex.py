#l1 = [10,20,30,40,50]

# map method
def sqr(num1):
    return num1 * num1

def addlists(arg1, arg2):
    return arg1 + arg2

l1 = [10,20,30,40,50,60,3,4]
l2 = [1,2,3,4,5,6,7]

l3 = list(map(addlists,l1,l2))
print(l3)



