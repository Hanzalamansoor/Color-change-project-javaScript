
class Employee : #Main parent class or base class 
     a = 1

class Programmer(Employee): #Inherited from the Employee class
    b = 2

class Manager(Programmer): #Inherited by the programmer class wich was inherited by the Employee class 
    c = 3


o = Employee()
print(o.a)

o = Programmer()
print(o.a,o.b)

o = Manager()
print(o.a,o.b,o.c)
