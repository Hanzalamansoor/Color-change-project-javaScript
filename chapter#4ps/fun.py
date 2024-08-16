#Write a program that takes 10 numbers as input from the user and stores them in a list. Then, print the list.
# numbers = []

# n1 = int(input(("Enter the number :")))
# numbers.append(n1)

# n2 = int(input(("Enter the number :")))
# numbers.append(n2)

# n3 = int(input(("Enter the number :")))
# numbers.append(n3)

# n4 = int(input(("Enter the number :")))
# numbers.append(n4)

# n5 = int(input(("Enter the number :")))
# numbers.append(n5)

# n6 = int(input(("Enter the number :")))
# numbers.append(n6)

# n7 = int(input(("Enter the number :")))
# numbers.append(n7)

# n8 = int(input(("Enter the number :")))
# numbers.append(n8)

# n9 = int(input(("Enter the number :")))
# numbers.append(n9)

# n10 = int(input(("Enter the number :")))
# numbers.append(n10)



# print("the final 10 numbers entered by the users :",numbers)



#Create a list of numbers from 1 to 10. Using list slicing, print the first 5 numbers, the last 5 numbers, and every alternate number in the list.

# Create a list of numbers from 1 to 10
# numbers = [1,2,3,4,5,6,7,8,9,10,11]

# print("last five number of the list,", numbers[5:])


# print("First five number of the list,", numbers[:5])

# print("Every alternative number  of the list,", numbers[::5])


#Write a program that prompts the user to enter 5 names and stores them in a list. Sort the list alphabetically and print it.
#Extend the previous program to allow the user to enter a name to search for in the list. Print whether the name is found or not.





Names = []
n1 = input("Enter the first person name :  ")
Names.append(n1)

n2 = input("Enter the first person name :  ")
Names.append(n2)

n3 = input("Enter the first person name :  ")
Names.append(n3)

n4 = input("Enter the first person name :  ")
Names.append(n4)

n5 = input("Enter the first person name :  ")
Names.append(n5)

Names.sort()
print(Names)



search_name = input("Enter a name to search for :")

if  search_name in Names:
    print(f"{search_name} Found in the list")
else :
    print(f"{search_name} is not founded")