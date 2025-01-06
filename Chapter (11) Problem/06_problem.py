# Write __str__()method to print the vector as follows:
#  7i + bj +10k
# Assume vector of dimension 3 for this problem.

class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
# Test the implementation
v1 = vector(1,2,3)
v2 = vector(4,5,6)
v3 = vector(7,8,9) # same dimension vector

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)