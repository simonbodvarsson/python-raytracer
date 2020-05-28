import unittest

import hittable
from vec3 import Vec3


class TestRay(unittest.TestCase):
    def test_hit_record(self):
        hr = hittable.HitRecord(Vec3(1, 1, 1), Vec3(1, 2, 3), 2)
