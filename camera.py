import math

from ray import Ray
from vec3 import Vec3


class Camera:
    def __init__(self, vfov=60, look_from=Vec3(-2, 2, 1), look_at=Vec3(0, 0, -1), view_up=Vec3(0, 1, 0),
                 aspect_ratio=16 / 9, aperture=2.0, focus_dist=None):
        self.vfov = vfov
        self.aspect_ratio = aspect_ratio
        self.aperture = aperture
        if focus_dist is None:
            self.focus_dist = (look_from - look_at).length()
        else:
            self.focus_dist = focus_dist

        theta = vfov * math.pi / 180
        h = math.tan(theta / 2)

        # Set height of the viewport to 2 units
        self.viewport_height = 2.0 * h
        self.viewport_width = self.aspect_ratio * self.viewport_height
        # Set distance from camera center (or eye) to viewport to 1 unit (in Z coordinate).
        self.focal_length = 1.0

        w = (look_from - look_at).unit_vector()
        u = view_up.cross(w).unit_vector()
        v = w.cross(u)
        self.u = u
        self.v = v
        self.w = w

        self.origin = look_from
        self.horizontal = self.focus_dist*self.viewport_width*u
        self.vertical = self.focus_dist*self.viewport_height * v
        self.lower_left_corner = self.origin - self.horizontal/2 - self.vertical/2 - self.focus_dist*w
        self.lens_radius = aperture / 2

    def get_ray(self, u, v):
        rd = self.lens_radius * Vec3.random_in_unit_disk()
        offset = u * rd.x + v * rd.y

        return Ray(self.origin+offset, self.lower_left_corner + u * self.horizontal + v * self.vertical - self.origin - offset)
