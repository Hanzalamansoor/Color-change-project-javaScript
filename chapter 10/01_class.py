# Class is just like an empty form with different placeholders 
# But when you write a code in the class it becomes object so class is blueprint for the object

#This is a class
class Employee:

    profession = "programmer" #This is a class attribute
    salary = 1200000



#This is an object
hanzala = Employee()
hanzala.name = "Hanzala Mansoor" # This is an object attribute (also called instance attribute)
print(hanzala.name,hanzala.profession,hanzala.salary)

umer = Employee()
umer.name = "Umer masnoor"
print( umer.name,umer.profession,umer.salary)
#Now here name attribute(also called instance attribute) belongs to the object and 
#profession and salary attributes belongs to the class attributes becuase 
#they are directly taken from the class where name attribute is created later in object