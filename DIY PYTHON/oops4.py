import random
class calculator :
    def __init__(self,n):
        self.n = n
        

    def addition(self) :
                  print(f"The addition of 5 with random no is {self.n + random.randint(1,5)}")

    def multiplication(self) :
                print(f"The multiplication of 5 with random number is {self.n * random.randint(1,5)}")


    def division(self) :
                random_number = random.randint(1, 5)

                print(f"The divison of 5 with random number is  {self.n// random_number }")


solve = calculator(5)
solve.addition()
solve.multiplication()
solve.division()
