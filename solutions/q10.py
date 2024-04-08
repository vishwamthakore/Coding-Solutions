# https://www.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1
#User function Template for python3

class Solution:
    
    def twoSum(self, remainingArr, target, skip):
        s = set()
        
        for i in range(len(remainingArr)):
            if target - remainingArr[i] in s:
                return True
                
            else:
                s.add(remainingArr[i])
        
        return False
        
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        
        for i in range(len(arr)):
            target = arr[i] * -1
            remainingArr = arr[:]
            remainingArr.pop(i)
            skip = i
            flag = self.twoSum(remainingArr, target, skip)
            if flag == True:
                return 1
                
        
        return 0