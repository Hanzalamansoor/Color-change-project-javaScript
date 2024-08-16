# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class attributes :
    a = 45

object = attributes()
object.a = 0
print(object.a) 



#No class attribute a=45 will stay 45 

