'''
snake : 1
water : -1
gun : 0
'''

import random
computer = random.choice([1,-1,0])
youStr = input("Enter your choice : ")
youDict = {"s": 1,"w": -1, "g": 0 }
reverseDict = {1: "s", -1: "w", 0:"g"}

you = youDict[youStr]

print(f"You chose : {reverseDict[you]}\n Computer chose : {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")
    # computer choice == -1 (water)
elif(computer == -1 and you == 1):
    print("You win!")

elif(computer == -1 and you == 0):
    print("You lose!")
    # computer chose == 1 (snake)
  
elif(computer == 1 and you == -1):
    print("You lose!")

elif(computer == 1 and you == 0):
    print("You win!")
    # computer chose == 0 (gun)
  
elif(computer == 0 and you == -1):
    print("You win!")

elif(computer == 0 and you == 1):
    print("You lose!")

else:
    print("Something went wrong")