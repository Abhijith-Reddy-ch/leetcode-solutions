class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n<= 1:
            return nums

        m = n//2
        L = self.sortArray(nums[:m])
        R = self.sortArray(nums[m:])

        l,r = 0,0
        l_len = len(L)
        r_len = len(R)
        ans = [0]*n
        i = 0

        while l<l_len and r <r_len:
            if L[l] < R[r]:
                ans[i] = L[l]
                l += 1
            else:
                ans[i] = R[r]
                r += 1
            
            i += 1
        
        while l<l_len:
            ans[i] = L[l]
            l+= 1
            i+=1
        while r<r_len:
            ans[i] = R[r]
            r += 1
            i+= 1

        return ans