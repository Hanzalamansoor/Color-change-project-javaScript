
class Employee : #Main parent class or base class
     def __init__(self) :
        print("Constructor of Employee")
          
     a = 1

class Programmer(Employee): #Inherited from the Employee class
       def __init__(self) :
           print("Constructor of Programmer")
       b = 2

class Manager(Programmer): #Inherited by the programmer class wich was inherited by the Employee class 
      def __init__(self) :
                 super().__init__() #super() method is used to access the methods of a super class in the derived class.


                 print("Constructor of Manager")
      c = 3




o = Manager()
print(o.a,o.b,o.c)
