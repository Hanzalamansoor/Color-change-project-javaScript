#. Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter the number :"))

i = 1
sum = 0

while(i<=n):  # if 10 is entered then all the value will add till 10
    sum += i  # sum + 1 , sum+2 
    i+=1  
    print(sum)