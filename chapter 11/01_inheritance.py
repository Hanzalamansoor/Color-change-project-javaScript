#Parent class or base class
class Employee :
    company = "ITC"

    def __init__(self,name,age,salary):
      self.name = name
      self.age = age 
      self.salary = salary

    def show(self):
        print(f"The name of the employee is {self.name} and the salary of the employee is : {self.salary}")



#child class or inherited class 
class programmer(Employee):
    company = "ITC info-tech"
    def show_language(self):
            print(f"The name of the employee is {self.name} and the salary of the employee is : {self.salary}")


a = Employee("Ali",25,500000)
print(a.name,a.age)

b = programmer("Umer",25,500000) #Taking name and age variable from parent class Employee
print(b.name,b.age)
b.show_language()


print(a.company,b.company)