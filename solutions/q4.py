# 88
# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums3 = nums1

        temp1 = nums1[:m]
        print(temp1)

        i=0
        j=0
        k=0
        while(i < len(temp1) and j < len(nums2)):
            if temp1[i] <= nums2[j]:
                nums3[k] = temp1[i]
                i+=1
                k+=1

            else:
                nums3[k] = nums2[j]
                k+=1
                j+=1

        while(i < len(temp1)):
            nums3[k] = temp1[i]
            k+=1
            i+=1
        
        while(j < len(nums2)):
            nums3[k] = nums2[j]
            k+=1
            j+=1