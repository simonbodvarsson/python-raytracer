# vec3 is a 3d vector and can hold 3d coordinates, color etc.
class Vec3:
    def __init__(self, x, y, z):
        self.vec = (x,y,z)
        self.__update_coordinates__()

    # Helper function to update x, y, z values
    def __update_coordinates__(self):
        self.x = self.vec[0]
        self.y = self.vec[1]
        self.z = self.vec[2]

    def length(self):
        return self.length_squared()**(0.5)

    def length_squared(self):
        return self.x**2 + self.y**2 + self.z**2

    # Overload operators +, -, [], +=, -=, *=, /=

    # Sum vectors
    def __add__(self, other):
        return Vec3(self.x+other.x, self.y+other.y, self.z+other.z)

    # Subtract vectors
    def __sub__(self, other):
        return Vec3(self.x-other.x, self.y-other.y, self.z-other.z)

    # Negate vector
    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    # Index vector
    def __getitem__(self, index):
        return self.vec[index]
    
    # Add a vector to this vector (override +=)
    def __iadd__(self, other):
        self.vec = (self.x+other.x, self.y+other.y, self.z+other.z)
        self.__update_coordinates__()
        return self

    # Subtract a vector from this vector (override -=)
    def __isub__(self, other):
        self.vec = (self.x-other.x, self.y-other.y, self.z-other.z)
        self.__update_coordinates__()
        return self

    # Multiply this vector by a constant t (override *=)
    def __imul__(self, t):
        self.vec = (self.x * t, self.y * t, self.z * t)
        self.__update_coordinates__()
        return self

    # Divide this vector by a constant t (override /=)
    def __itruediv__(self, t):
        if t == 0:
            raise ZeroDivisionError
        self.vec = (self.x / t, self.y / t, self.z / t)
        self.__update_coordinates__()
        return self
    
    # Overload str()
    def __str__(self):
        return str(self.vec)