https://leetcode.com/problems/palindrome-number/solution/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math
        isp = False
        if(x < 0 or (x % 10 == 0 and x != 0)):
            return False

        rn = 0
        while x > rn :
            rn = rn * 10 + x %10
            x /=10

        return x == rn or x == rn/10
