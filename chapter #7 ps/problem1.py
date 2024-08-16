# Write a program to print multiplication table of a given number using for loop

number = int(input("Enter a number to multiply :"))  # Ask user to enter a specific number you want a table of

for i in range (1,11) :  # (that number x 1,11)
   result =  number * i

   print(f"{number} x {i} = {result}")


