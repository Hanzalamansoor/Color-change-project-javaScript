a = (45,453,87,True,"Roberts","Marston")
print(type(a))

no = a.count(45)
print(no)  # it will count how many times 45 is in the tuple 

i = a.index(453)
print(i)

d = len(a)
print(d)


tuple1 = (1,2,3,4,5,6)
tuple2 = (7,8,9,10,11,12)

concatination = tuple1 + tuple2
print(concatination)