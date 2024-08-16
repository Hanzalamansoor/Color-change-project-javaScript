class Employee:
    def __init__(self, salary=12000, increment=20):
        self.salary = salary
        self.increment = increment

    @property
    def salaryafterincrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryafterincrement.setter
    def salaryafterincrement(self, salary):
        self.increment = ((salary / self.salary) - 1) * 100

e = Employee()
e.salaryafterincrement = 14400  # Changed target salary to 14400 to match the increment calculation
print(e.increment)  # Output the increment percentage


#Explanation of this code : 
# Sure! Let’s break down the Employee class program step-by-step in simple terms:

# Code Breakdown
# Class Definition:

# python
# Copy code
# class Employee:
# This line creates a new class called Employee. Think of a class like a blueprint for creating objects (like a detailed plan for building a house).
# Initialization (__init__ Method):

# python
# Copy code
# def __init__(self, salary=12000, increment=20):
#     self.salary = salary
#     self.increment = increment
# __init__ is a special method that sets up the initial state of a new Employee object.
# salary=12000 and increment=20 are default values. If you don’t provide these values when creating an Employee object, it will use 12000 and 20 by default.
# self.salary and self.increment store the salary and increment percentage for the Employee object. self refers to the specific instance of the class.
# Property Getter (@property):

# python
# Copy code
# @property
# def salaryafterincrement(self):
#     return self.salary + self.salary * (self.increment / 100)
# @property is a decorator that makes a method behave like an attribute (a piece of data you can access directly).
# salaryafterincrement is a method that calculates the salary after adding the increment.
# self.salary * (self.increment / 100) calculates how much the salary increases based on the increment percentage.
# self.salary + ... adds the increment to the original salary.
# Property Setter (@<property_name>.setter):

# python
# Copy code
# @salaryafterincrement.setter
# def salaryafterincrement(self, salary):
#     self.increment = ((salary / self.salary) - 1) * 100
# @salaryafterincrement.setter allows you to set the salaryafterincrement property.
# salary is the new salary you want to set.
# self.increment is updated to show the percentage increase needed to reach the new salary from the original salary.
# Creating an Employee Object and Using It:

# python
# Copy code
# e = Employee()
# e.salaryafterincrement = 14400
# print(e.increment)
# e = Employee() creates a new Employee object with default values (salary 12000 and increment 20%).
# e.salaryafterincrement = 14400 sets the target salary to 14400. This triggers the setter method, which calculates and updates the increment to achieve this target salary.
# print(e.increment) displays the increment percentage needed to reach the target salary.
# Summary for Beginners
# Class: A template to create objects. Here, Employee is the class.
# Initialization: Sets up new objects with starting values (salary and increment).
# Properties: Special methods that make it easy to get and set values like attributes.
# Getter: Calculates the new salary after applying the increment.
# Setter: Updates the increment needed to reach a new target salary.
# This program helps manage and calculate salary changes easily by using properties to control how salary and increment are set and retrieved. 