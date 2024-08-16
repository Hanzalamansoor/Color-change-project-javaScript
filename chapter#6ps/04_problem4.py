# Write a program to find whether a given username contains less than 10
# characters or not.

username = input("Enter the username :")
if(len(username)>10) :
    print("Your name contains more then 10 charachetrs ")
elif (len(username)<10) :
    print("Your entered name contains less than 10 characters")
