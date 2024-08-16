class new :
    b = 8
    @classmethod # Now after adding class method this class attribute will be prefered 
    def new(cls):
                print(f"The class attribute is {cls.b} ")
    
    @property
    def name (self):
            return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
            self.fname = value.split(" ")[0]
            self.lname = value.split(" ")[1]
   #final result = ["Hanzla", "Mansoor"]



f = new()
f.name = "Hanzala Mansoor"
print(f.lname)

#So basically we use properties decorator to control our instance attributes 
#In the above program we can print the first name accoring to our wish and last name whenever we want to print it or both from the instance variable 