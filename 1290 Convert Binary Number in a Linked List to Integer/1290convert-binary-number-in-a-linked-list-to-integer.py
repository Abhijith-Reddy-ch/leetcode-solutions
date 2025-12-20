class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        stack = []
        curr = head

        while curr:
            stack.append(curr.val)
            curr = curr.next

        ans = 0
        n = len(stack) - 1

        for bit in stack:          # MSB → LSB
            ans += bit * (2 ** n)
            n -= 1

        return ans
