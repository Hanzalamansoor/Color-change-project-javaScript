#Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    
     def __init__(self,r,i) :
            self.r = r
            self.i = i
            

     def __add__(self, c2):
           return  Complex(self.r + c2.r, self.i +c2.i)
     
     
     def __mul__(self, c2):
        # Multiplication of two complex numbers
        real_part = (self.r * c2.r) - (self.i * c2.i)
        imaginary_part = (self.r * c2.i) + (self.i * c2.r)
        return Complex(real_part, imaginary_part)


     def __str__(self):
         return f"{self.r} + {self.i}i"
           
      

c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1 + c2)

print(f"Addition: {c1 + c2}")  # Output: Addition: 4 + 6i
print(f"Multiplication: {c1 * c2}")  # Output: Multiplication: -5 + 

        