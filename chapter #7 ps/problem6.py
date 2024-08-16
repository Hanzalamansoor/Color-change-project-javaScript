#6. Write a program to calculate the factorial of a given number using for loop.


#factorial means 5! = 1x2x3x4x5


n = int(input("Enter the number : "))

product = 1 

for i in range (1,n+1) :

    product = product * i
print(f"The factorial of {n} is {product}")

# it works like product = product * i, product = 1 * 1 = 1 so product saves 1 and move forward like product = 1*2=2 and product saves 3 and move forward like product = 2*3 = 6 