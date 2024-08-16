#Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        # Vector addition: (x1 + x2, y1 + y2, z1 + z2)
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        # Dot product: x1*x2 + y1*y2 + z1*z2
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

# Print the results of addition and dot product
print("v1 + v2:", v1 + v2)  # Vector addition
print("v1 * v2:", v1 * v2)  # Dot product

print("v2 + v3:", v2 + v3)  # Vector addition
print("v2 * v3:", v2 * v3)  # Dot product
