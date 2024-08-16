#Parent class or base class
class Employee :
    company = "ITC"
    name = "Default name "
   

    def show(self):
        print(f"The name of the employee is {self.company} and the name of the employee is : {self.name}")

#This is the 2 parent class 
class programming_language():
     language = "Python"
    
     def print_language(self):
      print(f"The programming language chosen by the programmer is {self.language}")


#child class or inherited class 
class programmer(Employee,programming_language):
    company = "ITC info-tech"
    def show_language(self):
            print(f"The name of the employee is {self.name} and the company of employee is {self.company}. chosen Programming language is {self.language} ")


a = Employee()


b = programmer() #Taking name and age variable from parent class Employee
b.show_language()
b.print_language()



