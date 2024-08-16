# Write a program to print the following star pattern.
# * * *
# *   *                 for n = 3
# * * *

n = int(input("Enter the number :"))

for i in range (1,n+1):
    if(i==1 or i==n): # for first row and the last row depeanding on the number you entered leaving the middle part
        print("*" * n,end="") # * will multiply by 3 if n=3
    else:
        print("*",end = "") # first asteric(*) of the middle row
        print(" " * (n-2),end="") # creating space on the n numbr if " " * (3-2) = 1 row of space
        print("*",end="") #last asteric of the middle part 
    print("")    