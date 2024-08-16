'''
rock : -1
paper : 1
scissors : 0
'''
import random

youstr = input("Enter your choice :")
computer = random.choice([-1,1,0])
youDict = {"rock": -1 ,"paper": 1, "scissors":0}
reverseDict = {-1 :"rock", 1 : "paper", 0 : "scissors"}
you = youDict[youstr]

print(f"Your chose : {reverseDict[you]}\n Computer chose : {reverseDict[computer]} ")

if(computer == you):
    print("It's a draw")
    #computer == -1 (rock)
elif(computer== -1 and you == 1):
    print("You win")
elif(computer == -1 and you == 0):
    print("You lose")    

 #computer == 1 (paper)
elif(computer== 1 and you == -1):
    print("You lose")
elif(computer == 1 and you == 0):
    print("You win")    


 #computer == 0 (scissors)
elif(computer== 0 and you == -1):
    print("You win")
elif(computer == 0 and you == 1):
    print("You lose")
else : 
    print("There is something wrong ")    

