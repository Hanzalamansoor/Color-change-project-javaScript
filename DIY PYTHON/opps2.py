class sports():
    def __init__(self,name,age,height,record) :
        self.name = name
        self.age = age
        self.height = height
        self.record = record
    @staticmethod   
    def greet():
        print("Good evening friends!")



object = sports("Robert","28","5ft10inch","18-0")
print(object.name,object.age,object.height,object.record)
object.greet()
