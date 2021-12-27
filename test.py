# pyunit test
import unittest

# python3 -m unnittest test.py

class Test(unittest.TestCase):
    def test_1918(self):
        from class4.ex_1918_tree import solution

        self.assertEqual("ABC+*", solution("A*(B+C)"))
        self.assertEqual( "AB+", solution("A+B"))
        self.assertEqual("ABC*+", solution("A+B*C"))
        self.assertEqual("ABC*+DE/-", solution("A+B*C-D/E"))