class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        altitudes = [0]*(n+1)
        gain_sum = 0
        for i in range(n):
            gain_sum += gain[i]
            altitudes[i+1] += gain_sum
        
        return max(altitudes)