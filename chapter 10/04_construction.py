class Employee:

    profession = "programmer" 
    salary = 1200000
    
    def __init__(self,name,salary,language) : #This is called dunder method which is automatically called
       self.name = name
       self.salary = salary
       self.language = language
       print("Hello guys welcome ")        
    

    
    
    @staticmethod #This means greet is a static method that doesn't  need object to pass , this is also called a decorator
    def greet():   
        print("Good morning")



hanzala = Employee("Hanzala",1300000,"Python")
hanzala.greet()
print(hanzala.profession,hanzala.salary,hanzala.name,hanzala.language)



#Using __init__(self) : this method doesn't needed to be called in the object
#because it runs automatically, we can use this instead of  creating an instantanious attribute 
#in an object




