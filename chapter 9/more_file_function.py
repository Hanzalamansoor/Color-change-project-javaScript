f = open("new.txt")
# lines = f.readlines()
# print(lines,type(lines))

# Now we can do that for seperate lines as well 

# line1 = f.readline()
# print(line1,type(line1))

# line2 = f.readline()
# print(line2,type(line2))

# line3 = f.readline()
# print(line3,type(line3))

# f.close()


# we can also use while loop to make the process less cumbersome 

line = f.readline()
while(line !=  ""):
    print(line)
    line = f.readline()
