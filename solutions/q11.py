# https://www.geeksforgeeks.org/problems/square-root/1

#Complete this function
class Solution:
    def floorSqrt(self, x):
        if x == 1:
            return 1
        
        left = 0
        right = x//2
        
        while (left<=right):
            mid = (left + right)//2
            
            midSq = mid*mid
            
            if midSq < x:
                left = mid + 1
                
            elif midSq > x:
                right = mid - 1
                
            elif midSq == x:
                return mid
        
        
        return right    
            
        
    #Your code here