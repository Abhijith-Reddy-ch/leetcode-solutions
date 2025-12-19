class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next

        k = k % count
        if k == 0:
            return head

        curr = head
        for _ in range(count - k - 1):
            curr = curr.next

        new_head = curr.next
        curr.next = None

        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = head

        return new_head
