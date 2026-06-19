class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        ans = [0]*n
        max_candies = max(candies)
        for i in range(n):
            if candies[i]+extraCandies >= max_candies:
                ans[i] = True
            else:
                ans[i] = False
        
        return ans