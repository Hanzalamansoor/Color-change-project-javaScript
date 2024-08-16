                        # Snake,Water,Gun project
'''
Snake : 1
water : -1
Gun: 0
'''   
import random
print("Welcome to snake,water,gun game , select your choice : s,w,n")
computer = random.choice([-1,0,1])
youstr = input("Enter your choice :")
youDict = {"s": 1,"w": -1,"g":0}
reverseDict = {1:"s", -1:"w", 0:"g"} # converting number into snake,water,gun to the user output display what you have chosen and what computer have chosen

you=youDict[youstr] # The value input by the user in form of (w,s,g) will be then checked in youDict because each of the value contains a numerical value
print(f"you chose : {reverseDict[you]}\n computer chose : {reverseDict[computer]}")

if(computer==you):
    print("It's a draw!")

else :
     #If computer chose -1(water)
     if(computer==-1 and you==1):
          print("You win!")
          

     elif(computer==-1 and you==0):
          print("You lose!")
            
     #If computer chose 1(snake)
     elif(computer == 1 and you == -1):
          print("You lose!")

     elif(computer==1 and you == 0):
          print("You win!")
    
     #If computer chose 0(gun)
     elif(computer==0 and you ==-1):
          print("You lose!")

     elif(computer==0 and you == 1):
          print("You lose!")
    
     else:
          print("Select within (s(snake),w(water),g(gun))")
