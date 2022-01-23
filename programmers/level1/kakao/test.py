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

    @unittest.skip("solved")
    def test_신규_아이디_추천_1단계(self):
        from .ex_02 import level1
        
        new_id = "...!@BaT#*..y.abcdefghijklm"
        
        result = "...!@bat#*..y.abcdefghijklm"
        
        self.assertEqual(result, level1(new_id))

    @unittest.skip("solved")
    def test_신규_아이디_추천_2단계(self):
        from .ex_02 import level2
        
        new_id = "...!@bat#*..y.abcdefghijklm"
        
        result = "...bat..y.abcdefghijklm"
        
        self.assertEqual(result, level2(new_id)) 

    @unittest.skip("solved")
    def test_신규_아이디_추천_3단계(self):
        from .ex_02 import level3
        
        new_id = "...bat..y.abcdefghijklm"
        
        result = ".bat.y.abcdefghijklm"
        
        self.assertEqual(result, level3(new_id))
        
    @unittest.skip("solved")
    def test_신규_아이디_추천_4단계(self):
        from .ex_02 import level4
        
        new_id = ".bat.y.abcdefghijklm"
        
        result = "bat.y.abcdefghijklm"
        
        self.assertEqual(result, level4(new_id))
        
    @unittest.skip("solved")
    def test_신규_아이디_추천_5단계(self):
        from .ex_02 import level5
        
        new_id = "bat.y.abcdefghijklm"
        
        result = "bat.y.abcdefghijklm"
        
        self.assertEqual(result, level5(new_id))
        
    @unittest.skip("solved")
    def test_신규_아이디_추천_6단계(self):
        from .ex_02 import level6
        
        new_id = "bat.y.abcdefghijklm"
        
        result = "bat.y.abcdefghi"
        
        self.assertEqual(result, level6(new_id))
        
    @unittest.skip("solved")
    def test_신규_아이디_추천_7단계(self):
        from .ex_02 import level7
        
        new_id = "bat.y.abcdefghi"
        
        result = "bat.y.abcdefghi"
        
        self.assertEqual(result, level7(new_id))

    @unittest.skip("solved")
    def test_신규_아이디_추천_01(self):
        from .ex_02 import solution
        
        new_id = "...!@BaT#*..y.abcdefghijklm"
        
        result = "bat.y.abcdefghi"
        
        self.assertEqual(result, solution(new_id))

    @unittest.skip("solved")
    def test_신규_아이디_추천_02(self):
        from .ex_02 import solution
        
        new_id = "z-+.^."
        
        result = "z--"
        
        self.assertEqual(result, solution(new_id))

    @unittest.skip("solved")
    def test_신규_아이디_추천_03(self):
        from .ex_02 import solution
        
        new_id = "=.="
        
        result = "aaa"
        
        self.assertEqual(result, solution(new_id))
        
    @unittest.skip("solved")
    def test_신규_아이디_추천_04(self):
        from .ex_02 import solution
        
        new_id = "123_.def"
        
        result = "123_.def"
        
        self.assertEqual(result, solution(new_id))
        
    @unittest.skip("solved")
    def test_신규_아이디_추천_05(self):
        from .ex_02 import solution
        
        new_id = "abcdefghijklmn.p"
        
        result = "abcdefghijklmn"
        
        self.assertEqual(result, solution(new_id))

    @unittest.skip("solved")
    def test_숫자_문자열과_영단어(self):
        from .ex_03 import solution
        
        s = ["one4seveneight", "23four5six7", "2three45sixseven", "123"]
        result = [1478, 234567, 234567, 123]
        
        for i in range(len(s)):
            self.assertEqual(result[i], solution(s[i]))
            
    @unittest.skip("solved")
    def test_크레인_인형뽑기_게임(self):
        from .ex_04 import solution
        
        board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
        moves = [1,5,3,5,1,2,1,4]
        result = 4
        
        self.assertEqual(result, solution(board, moves))

    @unittest.skip("solved")
    def test_실패율_01(self):
        from .ex_05 import solution
        
        N = 5
        stages = [2, 1, 2, 6, 2, 4, 3, 3]
        result = [3,4,2,1,5]
        
        self.assertEqual(result, solution(N, stages))

    @unittest.skip("solved")
    def test_실패율_02(self):
        from .ex_05 import solution
        
        N = 4
        stages = [4,4,4,4,4]
        result = [4,1,2,3]
        
        self.assertEqual(result, solution(N, stages))

    def test_1차_비밀지도_01(self):
        from .ex_06 import solution
        
        n = 5
        arr1 = [9, 20, 28, 18, 11]
        arr2 = [30, 1, 21, 17, 28]
        result = ['#####', '# # #', '### #', '#  ##', '#####']
        
        self.assertEqual(result, solution(n, arr1, arr2))

    def test_1차_비밀지도_02(self):
        from .ex_06 import solution
        
        n = 6
        arr1 = [46, 33, 33 ,22, 31, 50]
        arr2 = 	[27 ,56, 19, 14, 14, 10]
        result = ['######', '###  #', '##  ##', ' #### ', ' #####', '### # ']
        
        self.assertEqual(result, solution(n, arr1, arr2))

