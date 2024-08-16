#Write a program to print the following star pattern.
'''
  *
 ***
*****            #for n = 3

 '''
# Number of rows
n = int(input("Enter the number : "))

for i in range (1,n+1) :
        print(" " * (n-i), end="") # this is for space like 3-1 = 2 space at first row, then 3-2 = 1 then 1 space in 2 row and then 3-3 = 0 then 0 spaces in the 3
        print("*" * (2*i-1),end="") # * will multiply with the numer of times  it will be printed like (2*1-1) = 1 in first row , (2*2-1) = 3 in second row and (2*3-1) = 5 in the 3 row 
         # for new line 
        print("")
