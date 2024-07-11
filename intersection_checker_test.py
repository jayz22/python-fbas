import unittest
from intersection_checker import check_intersection
from fbas import QSet, FBAS

q1 = QSet.make(3, [1,2,3,4],[])
fbas1 = FBAS({1 : q1, 2 : q1, 3 : q1, 4 : q1})
q2 = QSet.make(2, [1,2,3,4],[])
fbas2 = FBAS({1 : q2, 2 : q2, 3 : q2, 4 : q2})


class IntersectionCheckerTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(check_intersection(fbas1))
        self.assertFalse(check_intersection(fbas2))
