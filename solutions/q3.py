# 7
# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x):
        rev = 0
        sign= 1 
        if x < 0:
            sign = -1

        x = x*sign

        while ((x != 0)):
            rev = rev * 10 + x % 10
            x //= 10
        
        rev = sign*rev

        int_max = 2**31 -1
        int_min = -2**31

        if rev >int_max or rev < int_min:
            return 0
        else:
            return rev