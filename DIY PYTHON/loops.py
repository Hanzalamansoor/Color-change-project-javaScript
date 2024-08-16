# n = int(input("Enter a number :"))
# for i in reversed ( range(1,11)) :
#     print({f"{n} X {i} = {n*i}"})


# t = [1,2,3,4,5,6,7]
# total_sum = 0

# for numbers in t :
#     total_sum += numbers
# print(total_sum)




# while loop 

# i=1
# number = int(input("Enter a number :"))
# while i<11 :   # condition to check that every time if it is true than it will continue the program otherwise the program will exit if the condition is false

#   result = number * i 
#   print(f"{number} X {i} = {result}")
#   i+=1
# print("End of the table")


# number = int(input("Enter a number :"))
# for i in range(1,11) :
#     result = number * i
#     print(f"{number}X{i} = {result}")



# n = int(input("Enter a number :"))

# for i in range (2,n) :
#     if(n%i == 0) :
#         print("This number is not a prime number")
#         break # so this will be stopped or it will not be                                                                                                                                                                                                                                          with the else statemnt 
#     else :
#         print("This is a prime number")




# adding all natural numbers input by the user

# n = int(input("Enter a number :"))

# i = 1
# sum = 0

# while(i<=n):
#     sum+=i
#     i+=1
# print(sum)



n = int(input("Enter a number : "))

product = 1

for i in range (1,n+1) :
    p = product * i
print(f"The factorial of {n} is {p} ")