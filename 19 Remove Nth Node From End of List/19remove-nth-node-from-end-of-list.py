# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return 

        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next

        curr = head
        curr_count = 0

        if count == n:
                head = curr.next

        while curr:
            if curr_count+1 == count-n:
                if curr.next.next:
                    curr.next = curr.next.next
                else:
                    curr.next = None
            curr = curr.next
            curr_count += 1
        return head