s = {12, 15, 32, 64,"BOB"} 
# print(s,type(s))
s.add("45") # this  will add another number or string 
print(s) 

# properties of sets 
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.

s.remove(64)
print(s)