# filter

def even(num1):
    if num1 % 2 == 0:
        return True
    else:
        return False 
l = [10,20,30,45,15,35,45,80]
f = list(filter(even,l))

print(f)

