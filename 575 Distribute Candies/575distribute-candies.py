class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        cset = set(candyType)
        return min(len(cset),len(candyType)//2)