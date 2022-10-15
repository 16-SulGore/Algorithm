from curses.ascii import isalnum

class Solution(object):
    def isPalindrome(self, str):
        str_list = []
        for s in str:
            if s.isalnum():
                str_list.append(s.lower())
        
        while len(str_list) > 1:
            if str_list.pop(0) != str_list.pop():
                return False
        return True
