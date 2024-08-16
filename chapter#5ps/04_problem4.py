#What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') ## length of s after these operations
print(len(s)) # len of s will be 2 because 20 == 20.0 which is true and set will only return the value once of the same value 
