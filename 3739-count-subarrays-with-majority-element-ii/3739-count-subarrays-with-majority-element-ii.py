class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        arr = [0]*(n*2+1)
        arr[n] = 1

        cnt = n
        ans = 0
        presum = 0
        for x in nums:
            if x == target:
                presum += arr[cnt]
                cnt += 1
                arr[cnt] += 1
            else:
                cnt -= 1
                presum -= arr[cnt]
                arr[cnt] += 1
            
            ans += presum
        
        return ans
