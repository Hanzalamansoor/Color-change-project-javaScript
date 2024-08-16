#Create a class “Programmer” for storing information of few programmers
# working at Microsoft

class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("Ali",1200000,12589)
print(p.name,p.salary,p.pin,p.company)
u = programmer("Umer",1300000,12569)
print(u.name,u.salary,u.pin,u.company)




        




