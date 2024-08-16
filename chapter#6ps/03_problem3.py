#A spam comment is defined as a text containing following keywords:
# "Make a lot of money”, "buy now”, "subscribe this”, "click this”. Write a program
# to detect these spams

# Define spam keywords
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

# Input a comment from the user
message = input("Enter a comment: ")

# Check if any of the spam keywords are in the message
if p1 in message or p2 in message or p3 in message or p4 in message:
    print("This is a spam")
else:
    print("This is not a spam")
