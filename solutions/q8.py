# 141
# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        nodes = set()
        node = head
        while node is not None:
            nodes.add(node)
            if node.next in nodes:
                return True
            
            node = node.next

        return False