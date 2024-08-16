#oops in python 
#class = cars 
class cars:
    def __init__(self,name,model,color,price):
        self.name = name
        self.model = model
        self.color = color 
        self.price = price 

    def run(self) :
        print(f"The car :{self.name} is runnimg")
    
    def stopped (self):
        print(f"the car :{self.name} is stopped")
    @staticmethod
    def greetings():
        print("Hello good morning")

object = cars("Civic",2024,"black",6500000)
object.greetings()
print(f"Car name :{object.name},car model :{object.model},car color : {object.color}, car price :{object.price}")
object.run()
object.stopped()

object1 = cars("Crolla",2024,"white",5000000)
print(f"Car name :{object1.name},car model :{object1.model},car color :{object1.color}, car price :{object1.price}")
object1.run()
object1.stopped()

