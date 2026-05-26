class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l,r = i+1,n-1
            while l<r:
                add = nums[l]+nums[r]+nums[i]
                if add==0:
                    ans.append((nums[r],nums[l],nums[i]))
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif add<0:
                    l+=1
                else:
                    r-=1
                    
        return ans
