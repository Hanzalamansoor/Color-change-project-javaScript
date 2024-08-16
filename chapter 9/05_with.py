f = open("file.txt")
print(f.read())
f.close()

# The same can be written without f.close():

with open("file.txt") as f :
    print(f.read())
 # You dont have to explicitly close the file using with statement 
 
