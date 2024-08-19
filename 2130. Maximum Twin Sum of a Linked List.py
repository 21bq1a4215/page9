# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        l2=[]
        for k in range(len(l)//2):l2.append(l.pop(0)+l.pop())
        return max(l2)
        
