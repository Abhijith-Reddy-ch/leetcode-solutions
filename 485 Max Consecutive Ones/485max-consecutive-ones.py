class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        count = 0
        for num in nums:
            if num==1:
                count +=1
            else:
                maxi = max(maxi,count)
                count =0

        return(max(maxi,count))
