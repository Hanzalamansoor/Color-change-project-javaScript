# Write a recursive function to calculate the sum of first n natural numbers.
'''
***
** - for n = 3
*
'''
def pattern(n) :
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(5)