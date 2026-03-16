class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        arr = []
        curr = head

        while curr:
            count = 1
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
                count += 1

            if count == 1:
                arr.append(curr.val)

            curr = curr.next

        if len(arr)==0 :
            return None

        curr = head
        for val in arr:
            curr.val = val
            prev = curr
            curr = curr.next

        prev.next = None

        return head