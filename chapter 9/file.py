# File i/o = if you want your data to persist you will use file i/o otherwise your data will stay volatile and get deleted once the program is closed 
# Python program can read from the file or write in the file using file i/o

f = open("file.txt") # open your file 
data = f.read()  # f.read will read your file
print(data)
f.close() # when ever we open the file it is our duty to close it 
