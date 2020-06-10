import unittest
from vec3 import Vec3


class TestVec3(unittest.TestCase):

    def test_init(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(-2.0, 0, 3)
        v3 = Vec3(3.14, -20001020, 20001020)
        self.assertEqual(v1.vec, (1, 2, 3))
        self.assertEqual(v2.vec, (-2.0, 0, 3))
        self.assertEqual(v3.vec, (3.14, -20001020, 20001020))
        self.assertEqual(v1.x, 1)
        self.assertEqual(v1.y, 2)
        self.assertEqual(v1.z, 3)

    def test_dot(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(-2.0, 0, 13)
        self.assertAlmostEqual(v1.dot(v2), v2.dot(v1))
        self.assertAlmostEqual(v1.dot(v2), 37)

    def test_cross(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(-2.0, 0, 13)
        self.assertAlmostEqual(v1.cross(v2)[0], -1 * v2.cross(v1)[0])
        self.assertAlmostEqual(v1.cross(v2)[1], -1 * v2.cross(v1)[1])
        self.assertAlmostEqual(v1.cross(v2)[2], -1 * v2.cross(v1)[2])
        self.assertAlmostEqual(v1.cross(v2).vec[0], Vec3(26, -6 - 13, -4)[0])

    def test_eq(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(-2.0, 0, 13)
        self.assertTrue(v1 == v1)
        self.assertTrue(v2 == v2)
        self.assertFalse(v1 == v2)
        self.assertFalse(v2 == v1)
        v3 = Vec3(1, 2, 3)
        v4 = Vec3(-2.0, 0, 13)
        self.assertTrue(v1 == v3)
        self.assertTrue(v4 == v2)

    def test_length(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(-2.0, 0, 3)
        v3 = Vec3(3.14, -212, 21)
        self.assertAlmostEqual(v1.length(), 14 ** 0.5)
        self.assertAlmostEqual(v1.length_squared(), v1.length() ** 2)
        self.assertAlmostEqual(v2.length(), 13 ** 0.5)
        self.assertAlmostEqual(v2.length_squared(), v2.length() ** 2)
        self.assertAlmostEqual(v3.length(), 213.060694639)
        self.assertAlmostEqual(v3.length_squared(), v3.length() ** 2)

        # Test unit vector
        u1 = v1.unit_vector()
        b1 = u1 * v1.length()
        self.assertAlmostEqual(u1.length(), 1)
        self.assertAlmostEqual(b1.length(), v1.length())
        self.assertAlmostEqual(b1[0], v1[0])
        self.assertAlmostEqual(b1[1], v1[1])
        self.assertAlmostEqual(b1[2], v1[2])

    def test_add(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(-2.0, 0, 3)
        v3 = Vec3(3.14, -20001020, 20001020)
        self.assertAlmostEqual((v1 + v2).vec[0], (-1, 2, 6)[0])
        self.assertAlmostEqual((v1 + v2).vec[1], (-1, 2, 6)[1])
        self.assertAlmostEqual((v1 + v2).vec[2], (-1, 2, 6)[2])
        self.assertAlmostEqual((v1 + v3).vec[0], (4.14, -20001018, 20001023)[0])
        self.assertAlmostEqual((v1 + v3).vec[1], (4.14, -20001018, 20001023)[1])
        self.assertAlmostEqual((v1 + v3).vec[2], (4.14, -20001018, 20001023)[2])
        self.assertAlmostEqual((v2 + v3).vec[0], (1.14, -20001020, 20001023)[0])
        self.assertAlmostEqual((v2 + v3).vec[1], (1.14, -20001020, 20001023)[1])
        self.assertAlmostEqual((v2 + v3).vec[2], (1.14, -20001020, 20001023)[2])
        self.assertAlmostEqual((v1 + 7)[0], 8)
        self.assertAlmostEqual((v1 + 7)[1], 9)
        self.assertAlmostEqual((v1 + 7)[2], 10)
        self.assertAlmostEqual((v2 + (-3.2))[0], -5.2)
        self.assertAlmostEqual((v2 + (-3.2))[1], -3.2)
        self.assertAlmostEqual((v2 + (-3.2))[2], -0.2)

    def test_sub(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(-2.0, 0, 3)
        v3 = Vec3(3.14, -20001020, 20001020)
        self.assertAlmostEqual((v1 - v2).vec[0], 3)
        self.assertAlmostEqual((v1 - v2).vec[1], 2)
        self.assertAlmostEqual((v1 - v2).vec[2], 0)
        self.assertAlmostEqual((v1 - v3).vec[0], -2.14)
        self.assertAlmostEqual((v1 - v3).vec[1], 20001022)
        self.assertAlmostEqual((v1 - v3).vec[2], -20001017)
        self.assertAlmostEqual((v2 - v3).vec[0], -5.14)
        self.assertAlmostEqual((v2 - v3).vec[1], 20001020)
        self.assertAlmostEqual((v2 - v3).vec[2], -20001017)
        self.assertAlmostEqual((v1 - 7)[0], -6)
        self.assertAlmostEqual((v1 - 7)[1], -5)
        self.assertAlmostEqual((v1 - 7)[2], -4)
        self.assertAlmostEqual((v2 - (-3.2))[0], 1.2)
        self.assertAlmostEqual((v2 - (-3.2))[1], 3.2)
        self.assertAlmostEqual((v2 - (-3.2))[2], 6.2)

    def test_neg(self):
        self.assertEqual((-Vec3(1, 2, 3)).vec, (-1, -2, -3))
        self.assertEqual((-Vec3(0, 1, -1)).vec, (0, -1, 1))
        self.assertEqual((-Vec3(0.14, 220100, -1459.3)).vec, (-0.14, -220100, 1459.3))

    def test_get(self):
        v1 = Vec3(1, 2, 3)
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

        vsum += 2.0
        self.assertAlmostEqual(vsum[0], -198.3)
        self.assertAlmostEqual(vsum[1], 1.0007)
        self.assertAlmostEqual(vsum[2], 17)

    def test_isub(self):
        v1 = Vec3(0, -1, 2)
        v1 -= Vec3(-200.3, 0.0007, 13)
        vsum = Vec3(200.3, -1.0007, -11)

        self.assertAlmostEqual(v1[0], vsum[0])
        self.assertAlmostEqual(v1[1], vsum[1])
        self.assertAlmostEqual(v1[2], vsum[2])
        vsum -= 2.0
        self.assertAlmostEqual(vsum[0], 198.3)
        self.assertAlmostEqual(vsum[1], -3.0007)
        self.assertAlmostEqual(vsum[2], -13)

    def test_imul(self):
        correct = [(0, -1, 2.13), (0, 2, -4.26), (0, -0.25, 0.5325)]
        ts = [1, -2, 0.25]

        for i, t in enumerate(ts):
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

        for i, t in enumerate(ts):
            v = Vec3(0, -1, 2.13)
            v /= t
            self.assertAlmostEqual(v.vec[0], correct[i][0])
            self.assertAlmostEqual(v.vec[1], correct[i][1])
            self.assertAlmostEqual(v.vec[2], correct[i][2])

    def test_str(self):
        self.assertEqual(str(Vec3(0, -1, 2)), "(0, -1, 2)")
        self.assertEqual(str(Vec3(-0.14, 0, -0)), "(-0.14, 0, 0)")
