class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        result = float("-inf")
        arr_sum = 0

        for right in range(len(nums)):
            arr_sum += nums[right]

            if right-left+1 == k:
                avg = arr_sum/k
                result = max(result,avg)
                arr_sum -= nums[left]
                left +=1
        
        return result
