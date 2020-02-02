# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def test_invalid_a(self):
        self.assertEqual(classifyTriangle("Hello", 8 , 3), "InvalidInput")

    def test_invalid_b(self):
        self.assertEqual(classifyTriangle(3, "Large", 17), "InvalidInput")

    def test_invalid_c(self):
        self.assertEqual(classifyTriangle(2, 18, "Egg"), "InvalidInput")

    def test_negative_a(self):
        self.assertEqual(classifyTriangle(0, 4, 2), "InvalidInput")

    def test_negative_b(self):
        self.assertEqual(classifyTriangle(13, -4, 12), "InvalidInput")

    def test_negative_c(self):
        self.assertEqual(classifyTriangle(21, 42, -12), "InvalidInput")

    def test_isosceles_ab(self):
        self.assertEqual(classifyTriangle(5,5,7), "Isosceles")

    def test_isosceles_ac(self):
        self.assertEqual(classifyTriangle(5,7,5), "Isosceles")

    def test_isosceles_bc(self):
        self.assertEqual(classifyTriangle(5,7,7), "Isosceles")

    def test_notTriangle_a(self):
        self.assertEqual(classifyTriangle(17,1,2), "NotATriangle")

    def test_notTriangle_b(self):
        self.assertEqual(classifyTriangle(3,18,4), "NotATriangle")

    def test_notTriangle_c(self):
        self.assertEqual(classifyTriangle(5,6,20), "NotATriangle")

    def test_scalene(self):
        self.assertEqual(classifyTriangle(2,3,4), "Scalene")




if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

