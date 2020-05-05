from vec3 import Vec3

class Ray():
    # Define a ray from origin along direction
    def __init__(self, origin, direction):
        self.origin = origin
        self.dir = direction

    # Return the point on the ray t times along 
    # direction from origin.
    def at(self, t):
        return self.origin + self.dir *  t 