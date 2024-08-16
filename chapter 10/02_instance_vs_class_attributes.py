class Employee:

    profession = "programmer" #class attribute as a profession
    salary = 1200000


hanzala = Employee()
hanzala.profession = "Graphic designer" # instantiation attribute set as profession again
print(hanzala.profession,hanzala.salary)

#Explanation : In the upper scenario profession is again used as an attribute
#in the object which is called instantiation attribute, so the question is 
# which attribute will be prefered in the given scenario ? , so the answer is
#the instantiation attribute will be prefered in setting  or getting 