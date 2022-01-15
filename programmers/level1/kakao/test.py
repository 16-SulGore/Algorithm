import unittest

class Test(unittest.TestCase):
    
    @unittest.skip("solved")
    def test_신고_결과_받기_01(self):
        from .ex_01 import solution
        
        id_list = ["muzi", "frodo", "apeach", "neo"]
        report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
        k = 2
        
        result = [2, 1, 1, 0]
        
        self.assertEqual(result, solution(id_list, report, k))
    
    @unittest.skip("solved")
    def test_신고_결과_받기_02(self):
        from .ex_01 import solution
        
        id_list =["con", "ryan"]
        report = ["ryan con", "ryan con", "ryan con", "ryan con"]
        k = 3
        
        result = [0, 0]        

        self.assertEqual(result, solution(id_list, report, k))

    def test_신규_아이디_추천_01(self):
        from .ex_02 import solution
        
        new_id = "...!@BaT#*..y.abcdefghijklm"
        
        result = "bat.y.abcdefghi"
        
        self.assertEqual(result, new_id)

    def test_신규_아이디_추천_02(self):
        from .ex_02 import solution
        
        new_id = "z-+.^."
        
        result = "z--"
        
        self.assertEqual(result, new_id)

    def test_신규_아이디_추천_03(self):
        from .ex_02 import solution
        
        new_id = "=.="
        
        result = "aaa"
        
        self.assertEqual(result, new_id)
        
        
    def test_신규_아이디_추천_04(self):
        from .ex_02 import solution
        
        new_id = "123_.def"
        
        result = "123_.def"
        
        self.assertEqual(result, new_id)
        
    def test_신규_아이디_추천_05(self):
        from .ex_02 import solution
        
        new_id = "abcdefghijklmn.p"
        
        result = "abcdefghijklmn"
        
        self.assertEqual(result, new_id)