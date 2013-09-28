'''
Created on Sep 23, 2013

@author: Nguyen Thi Loan
'''
import unittest
import math
from triangle import detect_triangle

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(detect_triangle(5, 5, 5),'This is a Equilateral Triangle.')
    def test2(self):
        self.assertEqual(detect_triangle(10**-10, 10**-10, 10**-10),'This is a Equilateral Triangle.')
    def test3(self):
        self.assertEqual(detect_triangle(2**32-1, 2**32-1, 2**32-1),'This is a Equilateral Triangle.')
    def test4(self):
        self.assertEqual(detect_triangle(4, 4, 4*math.sqrt(2)),'This is a Right Isosceles Triangle.')
    def test5(self):
        self.assertEqual(detect_triangle(4, 4*math.sqrt(2), 4),'This is a Right Isosceles Triangle.')
    def test6(self):
        self.assertEqual(detect_triangle(3, 4, 5),'This is a Right Triangle.')
    def test7(self):
        self.assertEqual(detect_triangle(3, 5, 4),'This is a Right Triangle.')
    def test8(self):
        self.assertEqual(detect_triangle(5, 3, 4),'This is a Right Triangle.')
    def test9(self):
        self.assertEqual(detect_triangle(5, 5, 6),'This is a Isosceles Triangle.')
    def test10(self):
        self.assertEqual(detect_triangle(5, 6, 5),'This is a Isosceles Triangle.')
    def test11(self):
        self.assertEqual(detect_triangle(6, 5, 5),'This is a Isosceles Triangle.')
    def test12(self):
        self.assertEqual(detect_triangle(3, 7, 8),'This is a Scalene Triangle.')
    def test13(self):
        self.assertEqual(detect_triangle(1, 7, 8),'This is not a triangle!')
    def test14(self):
        self.assertEqual(detect_triangle(10**-9, 7, 8),'This is not a triangle!')
    def test15(self):
        self.assertEqual(detect_triangle('a', 7, 8),'The input is invalid! Please enter 3 integers from 0 to 2^32-1.')
    def test16(self):
        self.assertEqual(detect_triangle(0, 0, 0),'The input is invalid! Please enter 3 integers from 0 to 2^32-1.')
    def test17(self):
        self.assertEqual(detect_triangle(2**32, 2**32, 2**32),'The input is invalid! Please enter 3 integers from 0 to 2^32-1.')
    def test18(self):
        self.assertEqual(detect_triangle(2**32, 7, 8),'The input is invalid! Please enter 3 integers from 0 to 2^32-1.')
    def test19(self):
        self.assertEqual(detect_triangle('a', 'b', 'c'),'The input is invalid! Please enter 3 integers from 0 to 2^32-1.')
    def test20(self):
        self.assertEqual(detect_triangle('a', 'b', -1),'The input is invalid! Please enter 3 integers from 0 to 2^32-1.')
    def test21(self):
        self.assertEqual(detect_triangle(-3, -5, -4),'The input is invalid! Please enter 3 integers from 0 to 2^32-1.')
    def test22(self):
        self.assertEqual(detect_triangle(2**32, -2, 8),'The input is invalid! Please enter 3 integers from 0 to 2^32-1.')
    def test23(self):
        self.assertEqual(detect_triangle('a', 'b', 8),'The input is invalid! Please enter 3 integers from 0 to 2^32-1.')
    def test24(self):
        self.assertEqual(detect_triangle(-4, -7, 8),'The input is invalid! Please enter 3 integers from 0 to 2^32-1.')
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
