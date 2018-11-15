# lambda and map
l = [10,20,30,40,50]
m = list(map(lambda num1: num1 * num1,l))
print(m)

l2 = [10,20,30,40,50]
l3 = [1,2,3,4,5] 

evenlist = list(filter( lambda number: number%2 == 0 ,l3))
print(evenlist)

l4 = list(map(lambda num1,num2: num1 + num2, l2, l3))
print(l4)
