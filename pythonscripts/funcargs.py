def add_index(*args):
    print(args)
    print(args[0])
    l = []
    for value in range(len(args[0])):
        sum = 0
        for value1 in args:
            print(value1)
            sum = sum + value1[value]
        l.append(sum)
    return l
    
l1 = [10,20,30,40,50]
l2 = [1,2,3,4,5]
l3 = [100,200,300,400,500]

l4 = add_index(l1,l2,l3)
print(l4)
l5 = add_index(l1,l2,l3,l4)
print(l5)
l6 = add_index(l1,l2,l3,l4,l5)
print(l6)
