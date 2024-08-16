#6. Write a program to mine a log file and find out whether it contains ‘python’.


with open("log.txt") as f :
    content = f.read()

if "python" in content :
    print("Python word is found in the text")
else:
    print("Pyton word is not found in the text")