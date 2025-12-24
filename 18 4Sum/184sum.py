class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans_arr = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l,r = j+1,n-1
                while l<r:
                    ans = nums[i]+nums[j]+nums[l]+nums[r]

                    if ans == target:
                        ans_arr.append([nums[i],nums[j],nums[l],nums[r]])
                        l +=1
                        r-=1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    
                    if ans<target:
                        l+=1
                    elif ans>target:
                        r-=1
        return ans_arr
