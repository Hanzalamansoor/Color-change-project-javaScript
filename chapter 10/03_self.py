class Employee:

    profession = "programmer" 
    salary = 1200000
    
    def getInfo(self) : #object is passed here in the name of self 
        print(f"The profession is : {self.profession}.and salary is {self.salary}")
    
    @staticmethod #This means greet is a static method that doesn't  need object to pass , this is also called a decorator
    def greet():   
        print("Good morning")

hanzala = Employee()
hanzala.greet()
hanzala.getInfo()
# Employee.getInfo(hanzala)- The upper syntax is changed into this one /This is for the example



#self means to run the function or method in the object 
