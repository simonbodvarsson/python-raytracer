import unittest
from vec3 import Vec3
from ray import Ray

class TestRay(unittest.TestCase):
    def test_ray(self):
        orgs = [Vec3(0,0,0), Vec3(-1, 0, 2.3)]
        dirs = [Vec3(1,-1,1), Vec3(0,0,-0.1)]
        ts  = [0, 2, -1.2]
        for origin in orgs:
            for direction in dirs:
                r = Ray(origin, direction)

                # Test __init__ function
                self.assertAlmostEqual(r.origin[0], origin[0])
                self.assertAlmostEqual(r.origin[1], origin[1])
                self.assertAlmostEqual(r.origin[2], origin[2])
                self.assertAlmostEqual(r.dir[0], direction[0])
                self.assertAlmostEqual(r.dir[1], direction[1])
                self.assertAlmostEqual(r.dir[2], direction[2])

                # Test at function
                for t in ts:
                    self.assertAlmostEqual(r.at(t)[0], (origin + direction*t)[0])
                    self.assertAlmostEqual(r.at(t)[1], (origin + direction)[1])                    
                    self.assertAlmostEqual(r.at(t)[2], (origin + t*direction*t)[2])
