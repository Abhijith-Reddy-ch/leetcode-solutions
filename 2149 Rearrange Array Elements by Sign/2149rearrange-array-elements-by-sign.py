class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posIndex = 0
        negIndex = 1
        ans = [0] * len(nums)  
        for i in range(0,len(nums)):
            if(nums[i]<0):
                ans[negIndex] = nums[i]
                negIndex +=2
            else:
                ans[posIndex] = nums[i]
                posIndex +=2
        
        return ans