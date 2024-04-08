# https://www.geeksforgeeks.org/problems/peak-element/1

# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        
        if len(arr) == 0:
            return -1
            
        if len(arr) == 1:
            return 0
        
        for i in range(n):
            if i == 0 and arr[i+1] <= arr[i]:
                return i
                
            if i == n-1 and arr[i-1] <= arr[i]:
                return i
                
            if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
                return i
                
        
        return -1