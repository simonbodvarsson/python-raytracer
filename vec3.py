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

    # Return the dot product of this vector and vector v
    def dot(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    # Return the cross product of this vector and vector v
    def cross(self, v):
        coord = (self.y * v.z - self.z * v.y,
                 self.z * v.x - self.x * v.z,
                 self.x * v.y - self.y * v.x)
        return Vec3(*coord) 

    # Returns a unit vector in direction of this vector
    def unit_vector(self):
        return self / self.length()

    # Overload operators +, -, [], +=, -=, *=, /=

    # Sum vectors or add constant to vector
    def __add__(self, other):
        # If argument is not of type Vec3, try adding it to each coordinate
        if not isinstance(other, Vec3):
            return Vec3(self.x + other, self.y + other, self.z + other)
        return Vec3(self.x+other.x, self.y+other.y, self.z+other.z)

    # Adding is commutative
    __radd__ = __add__

    # Subtract vectors
    def __sub__(self, other):
        # If argument is not of type Vec3, try subtracting it from each coordinate
        if not isinstance(other, Vec3):
            return Vec3(self.x - other, self.y - other, self.z - other)
        return Vec3(self.x-other.x, self.y-other.y, self.z-other.z)

    # Multiply a vector by a constant t
    def __mul__(self, t):
        return Vec3(self.x * t, self.y * t, self.z * t)

    # Multiplication is commutative
    __rmul__ = __mul__
    
    # Divide a vector by a constant t
    def __truediv__(self, t):
        return Vec3(self.x / t, self.y / t, self.z / t)

    # Negate vector
    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    # Index vector
    def __getitem__(self, index):
        return self.vec[index]
    
    # Add a vector or constant to this vector (override +=)
    def __iadd__(self, other):
        # If argument is not of type Vec3, try adding it to each coordinate
        if not isinstance(other, Vec3):
            self.vec = (self.x+other, self.y+other, self.z+other)
        else:
            self.vec = (self.x+other.x, self.y+other.y, self.z+other.z)
        self.__update_coordinates__()
        return self

    # Subtract a vector or constant from this vector (override -=)
    def __isub__(self, other):
        if not isinstance(other, Vec3):
            self.vec = (self.x-other, self.y-other, self.z-other)
        else:
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

    # Two Vec3 are equal if their data is equal
    def __eq__(self, other):
        return self.vec == other.vec
    
    # Overload str()
    def __str__(self):
        return str(self.vec)