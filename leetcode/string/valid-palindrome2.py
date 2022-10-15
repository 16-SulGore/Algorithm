import collections

class Solution(object):
    def isPalindrome(self, str):
        strs = collections.deque()

        for s in str:
            if s.isalnum():
                strs.append(s.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True