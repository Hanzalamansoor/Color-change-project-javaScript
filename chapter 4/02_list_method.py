friends = ["Apple","Banana","Orange","Strawberry","mango"]
friends.append ("John Marston") # will include anything that you want to add in the end of the string
print(friends)
# append means in english is to add (something) to the end of a written document.


    # LIST METHODS.

l1 = [22,1,4,16,82,11,12,5,6,69]
l1.sort() # it will sort the list in increasing order starting from 1
print(l1) 

l1.reverse() # it will reverse the list from bigger number to the smaller one or in descending order
print(l1)


l1.insert(3,125) #it will add 125 at index 3
print(l1)

l1.pop(3) # will delete the number at index 3
print(l1)

print(l1.pop(3)) # will return the value of the deleted number like at index 3 number is 16 which is deleted so it will return number 16


l1.remove(22) # will remove particular number you want to remove without callinga an index just like in pop method
print(l1)

