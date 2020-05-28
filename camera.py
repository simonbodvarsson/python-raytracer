from ray import Ray
from vec3 import Vec3


class Camera:
    def __init__(self):
        self.aspect_ratio = 16 / 9

        # Set height of the viewport to 2 units
        self.viewport_height = 2.0
        self.viewport_width = self.aspect_ratio * self.viewport_height
        # Set distance from camera center (or eye) to viewport to 1 unit (in Z coordinate).
        self.focal_length = 1.0

        # Focal point
        self.origin = Vec3(0, 0, 0)
        self.horizontal = Vec3(self.viewport_width, 0, 0)
        self.vertical = Vec3(0, self.viewport_height, 0)
        self.lower_left_corner = self.origin - self.horizontal / 2 - self.vertical / 2 - Vec3(0, 0, self.focal_length)

    def get_ray(self, u, v):
        return Ray(self.origin, self.lower_left_corner + u*self.horizontal + v*self.vertical - self.origin)