import unittest
from vec3 import Vec3

class TestVec3(unittest.TestCase):
    
    def test_init(self):
        v1 = Vec3(1,2,3)
        v2 = Vec3(-2.0, 0, 3)
        v3 = Vec3(3.14, -20001020, 20001020)
        self.assertEqual(v1.vec, (1, 2, 3))
        self.assertEqual(v2.vec, (-2.0, 0, 3))
        self.assertEqual(v3.vec, (3.14, -20001020, 20001020))
        self.assertEqual(v1.x, 1)
        self.assertEqual(v1.y, 2)
        self.assertEqual(v1.z, 3)

    def test_add(self):
        v1 = Vec3(1,2,3)
        v2 = Vec3(-2.0, 0, 3)
        v3 = Vec3(3.14, -20001020, 20001020)
        self.assertAlmostEqual((v1+v2).vec[0], (-1, 2, 6)[0])
        self.assertAlmostEqual((v1+v2).vec[1], (-1, 2, 6)[1])
        self.assertAlmostEqual((v1+v2).vec[2], (-1, 2, 6)[2])
        self.assertAlmostEqual((v1+v3).vec[0], (4.14, -20001018, 20001023)[0])
        self.assertAlmostEqual((v1+v3).vec[1], (4.14, -20001018, 20001023)[1])
        self.assertAlmostEqual((v1+v3).vec[2], (4.14, -20001018, 20001023)[2])
        self.assertAlmostEqual((v2+v3).vec[0], (1.14, -20001020, 20001023)[0])
        self.assertAlmostEqual((v2+v3).vec[1], (1.14, -20001020, 20001023)[1])
        self.assertAlmostEqual((v2+v3).vec[2], (1.14, -20001020, 20001023)[2])

    def test_sub(self):
        v1 = Vec3(1,2,3)
        v2 = Vec3(-2.0, 0, 3)
        v3 = Vec3(3.14, -20001020, 20001020)
        self.assertAlmostEqual((v1-v2).vec[0], 3)
        self.assertAlmostEqual((v1-v2).vec[1], 2)
        self.assertAlmostEqual((v1-v2).vec[2], 0)
        self.assertAlmostEqual((v1-v3).vec[0], -2.14)
        self.assertAlmostEqual((v1-v3).vec[1], 20001022)
        self.assertAlmostEqual((v1-v3).vec[2], -20001017)
        self.assertAlmostEqual((v2-v3).vec[0], -5.14)
        self.assertAlmostEqual((v2-v3).vec[1], 20001020)
        self.assertAlmostEqual((v2-v3).vec[2], -20001017)

    def test_neg(self):
        self.assertEqual((-Vec3(1,2,3)).vec, (-1, -2, -3))
        self.assertEqual((-Vec3(0,1,-1)).vec, (0, -1, 1))
        self.assertEqual((-Vec3(0.14, 220100, -1459.3)).vec, (-0.14, -220100, 1459.3))

    def test_get(self):
        v1 = Vec3(1,2,3)
        v2 = Vec3(-2.0, 0, 3)
        v3 = Vec3(3.14, -20001020, 20001020)
        self.assertEqual(v1[0], 1)
        self.assertEqual(v1[1], 2)
        self.assertEqual(v1[2], 3)
        self.assertEqual(v3[0], 3.14)
        self.assertEqual(v3[1], -20001020)
        self.assertEqual(v3[2], 20001020)

    def test_iadd(self):
        v1 = Vec3(0, -1, 2)
        v1 += Vec3(-200.3, 0.0007, 13)
        vsum = Vec3(-200.3, -0.9993, 15)

        self.assertAlmostEqual(v1[0], vsum[0])
        self.assertAlmostEqual(v1[1], vsum[1])
        self.assertAlmostEqual(v1[2], vsum[2])
        self.assertAlmostEqual(v1.x, v1.vec[0])
        self.assertAlmostEqual(v1.y, v1.vec[1])
        self.assertAlmostEqual(v1.z, v1.vec[2])

    def test_isub(self):
        v1 = Vec3(0, -1, 2)
        v1 -= Vec3(-200.3, 0.0007, 13)
        vsum = Vec3(200.3, -1.0007, -11)

        self.assertAlmostEqual(v1[0], vsum[0])
        self.assertAlmostEqual(v1[1], vsum[1])
        self.assertAlmostEqual(v1[2], vsum[2])

    def test_imul(self):
        correct = [(0, -1, 2.13), (0, 2, -4.26), (0, -0.25, 0.5325)]
        ts = [1, -2, 0.25]

        for i,t in enumerate(ts):
            v = Vec3(0, -1, 2.13)
            v *= t
            self.assertAlmostEqual(v.vec[0], correct[i][0])
            self.assertAlmostEqual(v.vec[1], correct[i][1])
            self.assertAlmostEqual(v.vec[2], correct[i][2])

    def test_idiv(self):
        # Check if error is raised when we try to divide by 0
        with self.assertRaises(ZeroDivisionError):
            v = Vec3(0, -1, 2.13)
            v /= 0

        correct = [(0, -1, 2.13), (0, 0.5, -1.065), (0, -4, 8.52)]
        ts = [1, -2, 0.25]

        for i,t in enumerate(ts):
            v = Vec3(0, -1, 2.13)
            v /= t
            self.assertAlmostEqual(v.vec[0], correct[i][0])
            self.assertAlmostEqual(v.vec[1], correct[i][1])
            self.assertAlmostEqual(v.vec[2], correct[i][2])

    def test_str(self):
        self.assertEqual(str(Vec3(0,-1,2)), "(0, -1, 2)")
        self.assertEqual(str(Vec3(-0.14, 0, -0)), "(-0.14, 0, 0)")
