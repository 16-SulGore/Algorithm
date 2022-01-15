import re
import unittest

class Test(unittest.TestCase):
    
    def test_신고_결과_받기_01(self):
        from .ex_01 import solution
        
        id_list = ["muzi", "frodo", "apeach", "neo"]
        report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
        k = 2
        
        result = [2, 1, 1, 0]
        
        self.assertEqual(result, solution(id_list, report, k))
    
    def test_신고_결과_받기_02(self):
        from .ex_01 import solution
        
        id_list =["con", "ryan"]
        report = ["ryan con", "ryan con", "ryan con", "ryan con"]
        k = 3
        
        result = [0, 0]        

        self.assertEqual(result, solution(id_list, report, k))