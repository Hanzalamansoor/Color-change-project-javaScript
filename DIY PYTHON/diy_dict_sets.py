#Create a set s1 with elements {1, 2, 3} and another set s2 with elements {3, 4, 5}. Perform the following operations:
# Union of s1 and s2.
# Intersection of s1 and s2.
# Difference between s1 and s2.
# Symmetric difference between s1 and s2.

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))
print(s1.intersection(s2))
difference_s1_s2 = s1 -s2
print(difference_s1_s2)