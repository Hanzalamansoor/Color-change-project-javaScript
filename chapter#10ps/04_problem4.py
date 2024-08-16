# 4. Add a static method in problem 2, to greet the user with hello

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
    
    @staticmethod
    def greetings():
        print("Hello friends")

        
a = calculator(4)
a.greetings()
a.square()
a.cube()
a.square_root()
