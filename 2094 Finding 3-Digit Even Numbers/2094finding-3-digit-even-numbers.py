class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        n = len(digits)

        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or j == k:
                        continue
                    if digits[k] %2 == 0:
                        num = digits[i]*100+digits[j]*10+digits[k]
                        ans.add(num)
        return sorted(ans)