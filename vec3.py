# vec3 is a 3d vector and can hold 3d coordinates, color etc.
import math
from random import random


class Vec3:
    def __init__(self, x, y, z):
        self.vec = (x, y, z)
        self.__update_coordinates__()

    # Helper function to update x, y, z values
    def __update_coordinates__(self):
        self.x = self.vec[0]
        self.y = self.vec[1]
        self.z = self.vec[2]

    def length(self):
        return self.length_squared() ** (0.5)

    def length_squared(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

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

    # Reflect this vector against a surface normal n
    def reflect(self, n):
        return self - 2*self.dot(n)*n

    def unit_vector(self):
        return self / self.length()

    # Create a new random Vec3
    @staticmethod
    def random(minimum=None, maximum=None):
        # If a range is given, both minimum and maximum must be given.
        assert (minimum is None and maximum is None) or (minimum is not None and maximum is not None)

        # If no range is given, generate a vec3 with coordinates in the range [0,1]
        if minimum is None and maximum is None:
            return Vec3(random(), random(), random())
        else:
            x = minimum + (maximum - minimum) * random()
            y = minimum + (maximum - minimum) * random()
            z = minimum + (maximum - minimum) * random()
            return Vec3(x, y, z)

    # Generate a random point in the unit sphere
    @staticmethod
    def random_in_unit_sphere():
        # Use a rejection method, generate random coordinates in range [0,1] a point in the unit sphere is found.
        while True:
            point = Vec3.random(minimum=-1, maximum=1)
            if point.length_squared() < 1:
                return point

    # Generate a random point in the unit sphere with Lambertian distribution.
    @staticmethod
    def random_unit_vector():
        a = random() * 2*math.pi
        z = -1 + (1 + 1) * random()
        r = math.sqrt(1 - z**2)
        return Vec3(r*math.cos(a), r*math.sin(a), z)

    # Hemispherical scattering
    @staticmethod
    def random_in_hemisphere(normal):
        in_unit_sphere = Vec3.random_in_unit_sphere()
        if in_unit_sphere.dot(normal) > 0.0: # In the same hemisphere as the normal
            return in_unit_sphere
        else:
            return -in_unit_sphere

    def refract(self, n, refraction_ratio):
        cos_theta = (-1*self.unit_vector()).dot(n)
        r_out_parallel = refraction_ratio * (self + cos_theta*n)
        r_out_perp = -math.sqrt(1.0 - r_out_parallel.length_squared()) * n
        return r_out_parallel + r_out_perp

    # Overload operators +, -, [], +=, -=, *=, /=

    # Sum vectors or add constant to vector
    def __add__(self, other):
        # If argument is not of type Vec3, try adding it to each coordinate
        if not isinstance(other, Vec3):
            return Vec3(self.x + other, self.y + other, self.z + other)
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    # Adding is commutative
    __radd__ = __add__

    # Subtract vectors
    def __sub__(self, other):
        # If argument is not of type Vec3, try subtracting it from each coordinate
        if not isinstance(other, Vec3):
            return Vec3(self.x - other, self.y - other, self.z - other)
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    # Multiply a vector by a constant t
    def __mul__(self, t):
        if isinstance(t, Vec3):
            return Vec3(self.x * t.x, self.y * t.y, self.z * t.z)
        else:
            return Vec3(self.x * t, self.y * t, self.z * t)

    # Multiplication is commutative
    __rmul__ = __mul__

    # Divide a vector by a constant t
    def __truediv__(self, t):
        if isinstance(t, Vec3):
            return Vec3(self.x / t.x, self.y / t.y, self.z / t.z)
        else:
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
            self.vec = (self.x + other, self.y + other, self.z + other)
        else:
            self.vec = (self.x + other.x, self.y + other.y, self.z + other.z)
        self.__update_coordinates__()
        return self

    # Subtract a vector or constant from this vector (override -=)
    def __isub__(self, other):
        if not isinstance(other, Vec3):
            self.vec = (self.x - other, self.y - other, self.z - other)
        else:
            self.vec = (self.x - other.x, self.y - other.y, self.z - other.z)
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
