class Solution(object):
    def isPalindrome(self, str):
        str = str.lower()

        str = re.sub('[^a-z0-9]','',str)

        return str == str[::-1]