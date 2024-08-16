#. Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

with open("poems.txt") as f :
    text = f.read()
if "Twinkle" in text:
    print("Your file contains the word twinkle")
else :
    print("Your file doesn't contain the word twinkle")

