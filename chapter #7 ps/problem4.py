#Write a program to find whether a given number is prime or not

n = int(input("Enter the number :"))

for i in range(2,n) :
   if(n%i == 0):
      print("This number is not a prime number")
      break
print("Number is prime")   


#explaination : 
# dor examle n = 7
# i starts from 2 and goes up to 6 (i.e., range(2, 7)).
# For each i, the code checks if 7 % i == 0.
# Here’s how it checks:

# 7 % 2 is 1 (not 0), so 7 is not divisible by 2.
# 7 % 3 is 1 (not 0), so 7 is not divisible by 3.
# 7 % 4 is 3 (not 0), so 7 is not divisible by 4.
# 7 % 5 is 2 (not 0), so 7 is not divisible by 5.
# 7 % 6 is 1 (not 0), so 7 is not divisible by 6.
# If No Divisor is Found:

# Since 7 is not divisible by any number from 2 to 6, the loop completes without finding a divisor.
# The code then prints "Number is prime".