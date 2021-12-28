# pyunit test
import unittest

# python3 -m unnittest test.py


class Test(unittest.TestCase):
    @unittest.skip("solved")
    def test_1918(self):
        from class4.ex_1918 import solution

        self.assertEqual("ABC+*", solution("A*(B+C)"))
        self.assertEqual("AB+", solution("A+B"))
        self.assertEqual("ABC*+", solution("A+B*C"))
        self.assertEqual("ABC*+DE/-", solution("A+B*C-D/E"))

    @unittest.skip("solved")
    def test_5639(self):
        from class4.ex_5639 import solution
        node_list = [50, 30, 24, 5, 28, 45, 98, 52, 60]
        result_list = [5, 28, 24, 45, 30, 60, 52, 98, 50]

        self.assertEqual(result_list, solution(node_list))

    # -----dp 방식----
    @unittest.skip("solved")
    def test_11444(self):
        from class4.ex_11444_dp import solution
        n = 1000

        self.assertEqual(517691607, solution(n))

    @unittest.skip("solved")
    def test_11444_range17(self):
        from class4.ex_11444_dp import solution
        fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
                    55, 89, 144, 233, 377, 610, 987, 1597]

        for i in range(2, len(fib_list)):
            self.assertEqual(fib_list[i], solution(i))

    @unittest.skip("solved")
    def test_11444_time_limit(self):
        from class4.ex_11444_dp import solution
        max = 1000000000000000000 - 1
        solution(max)

    # ------분할 정복 방식-----
    @unittest.skip("solved")
    def test_11444(self):
        from class4.ex_11444_div_con import solution
        n = 1000

        self.assertEqual(517691607, solution(n))

    @unittest.skip("solved")
    def test_11444_range17(self):
        from class4.ex_11444_div_con import solution
        fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
                    55, 89, 144, 233, 377, 610, 987, 1597]

        for i in range(2, len(fib_list)):
            self.assertEqual(fib_list[i], solution(i))

    @unittest.skip("solved")
    def test_11444_time_limit(self):
        from class4.ex_11444_div_con import solution
        max = 1000000000000000000 - 1
        solution(max)

    def test_12865(self):
        from class4.ex_12865 import solution
        N, K = 4, 7
        backpack = [[6, 13], [4, 8], [3, 6], [5, 12]]
        result = 14
        
        self.assertEqual(result, solution(N, K, backpack))