# pyunit test
import unittest

# python3 -m unnittest test.py

class Test(unittest.TestCase):
    @unittest.skip("solved")
    def test_1918(self):
        from class4.ex_1918 import solution

        self.assertEqual("ABC+*", solution("A*(B+C)"))
        self.assertEqual( "AB+", solution("A+B"))
        self.assertEqual("ABC*+", solution("A+B*C"))
        self.assertEqual("ABC*+DE/-", solution("A+B*C-D/E"))
        
    def test_5639(self):
        from class4.ex_5639 import solution
        node_list = [50, 30, 24, 5, 28, 45, 98, 52, 60]
        result_list = [5, 28, 24, 45, 30, 60, 52, 98, 50]
        
        self.assertEqual(result_list, solution(node_list))
        