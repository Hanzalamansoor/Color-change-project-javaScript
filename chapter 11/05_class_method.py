# class Employee :
#     a = 5
#     def show(self):
#         print(f"The class attribute is {self.a} ")


# e = Employee()
# e.a = 45  # This will be prefered over class method a = 5 so to correct the problem we will use @classmethod
# e.show()




class new :
    b = 8
    @classmethod # Now after adding class method this class attribute will be prefered 
    def new(cls):
                print(f"The class attribute is {cls.b} ")

f = new()
f.b = 55
f.new()