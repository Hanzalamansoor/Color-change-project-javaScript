#: Write a program to print 1 to 50 using a while loop.
# i = 0

# while(i < 51) :
#     print(i)
#     i = i + 1

#Write a program to print the content of a list using while loops.

list = ["eggs","milk","vegetables","bread"]
i = 0
while( i < len(list)) : # length of list is 4 so first it starts ith 0,0<4 which is true it continues until 4<4 which is false so it will end  the program there
    print(list[i])
    i+=1