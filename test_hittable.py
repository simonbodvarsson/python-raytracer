import unittest

import hittable
import material
from vec3 import Vec3


class TestHittable(unittest.TestCase):
    def test_hit_record(self):
        hr = hittable.HitRecord(Vec3(1, 1, 1), Vec3(1, 2, 3), 2, material.Lambertian(Vec3(0.5, 0.5, 0.5)))
