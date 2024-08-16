#1. Write a program using functions to find greatest of three numbers.

def greatestnumebrs() :
    a = int(input("Enter a number a :"))
    b = int(input("Enter a number b :"))
    c = int(input("Enter a number c :"))
    if(a>b and a>c):
        return "a is the  greatest among 3"
    elif(b>a and b>c):
        return "b is the greatest amongst 3"
    elif(c>a and c>b):
        return "c is  the greatest amongst 3"


a = greatestnumebrs()
print(a)