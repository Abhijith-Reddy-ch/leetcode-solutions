# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
            
        curr = head
        low_arr = []
        high_arr = []
        while curr:
            if curr.val<x:
                low_arr.append(curr.val)
            else:
                high_arr.append(curr.val)
            curr = curr.next

        curr = head
        prev = None

        combined = low_arr + high_arr

        for val in combined:
            curr.val = val
            prev = curr
            curr = curr.next
        
        if prev:
            prev.next = None
        
        return head
        
