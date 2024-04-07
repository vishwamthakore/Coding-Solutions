# 78
# https://leetcode.com/problems/subsets/description/

class Solution:
    def solve(self, nums, left, right):
        print("left", left)
        if left > right:
            return [[]]
        else:
            subsets = self.solve( nums, left+1, right)

            subsets2 = []
            print(nums[left])
            for subset in subsets:
                t= subset[:]
                t.insert(0, nums[left])
                print("t", t)
                subsets2.append(t)

            # print("left", left, "subset", subset, "subsets2", subsets2)
            subsets.extend(subsets2)
            return subsets


    def subsets(self, nums: List[int]) -> List[List[int]]:
        left = 0
        right = len(nums) -1
        return self.solve(nums, left, right)

