class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        num1 = x
        s = 0
        while x > 0:
            r = x % 10
            s = s * 10 + r
            x = x // 10
        
        return num1 == s