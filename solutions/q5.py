# 112
# https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    total = 0
    target = 0
    ans = False
    def inorder(self, node):
        if self.ans == True:
            return 

        if node is None:
            return

        if node.left is None and node.right is None:
            if self.total + node.val == self.target:
                self.ans = True

        self.total = self.total + node.val
        self.inorder(node.left)
        self.inorder(node.right)
        self.total = self.total - node.val



    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.total = 0
        self.target = targetSum

        self.inorder(root)
        return self.ans

