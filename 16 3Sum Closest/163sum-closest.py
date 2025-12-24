class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        n = len(nums)

        for i in range(n):
            l,r= i+1,n-1

            while l<r:
                curr = nums[i]+nums[l]+nums[r]

                if abs(curr-target)<abs(closest-target):
                    closest = curr

                if curr<target:
                    l+=1
                elif curr>target:
                    r-=1
                else:
                    return curr
        return closest
