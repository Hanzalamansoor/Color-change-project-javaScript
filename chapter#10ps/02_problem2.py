# Write a class “Calculator” capable of finding square, cube and square root of a
# number.
import math
class calculator :
    def __init__(self,n) :
        self.n = n

    def square(self):
        print(f"The square of yout number is {self.n*self.n}")   

    def cube(self):
        print(f"The cube of your number is {self.n *self.n *self.n}")

    def square_root(self):
        print(f"The square root of your number is {math.sqrt(self.n)}") 

        
a = calculator(4)
a.square()
a.cube()
a.square_root()