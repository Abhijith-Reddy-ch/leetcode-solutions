# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        keep = []
        maxi = float("-inf")

        for i in range(len(arr)-1, -1, -1):
            if arr[i] >= maxi:
                keep.append(arr[i])
                maxi = arr[i]

        keep.reverse()

        dummy = ListNode(0)
        curr = dummy

        for val in keep:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
            
