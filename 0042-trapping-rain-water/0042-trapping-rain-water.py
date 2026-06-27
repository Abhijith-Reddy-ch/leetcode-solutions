class Solution:
    def trap(self, height: List[int]) -> int:
        '''n = len(height)
        ans = 0

        
        left_max,right_max = 0,0
        water = 0
        left,right = 0,n-1
        while left<right:
            if height[left]<height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left +=1
            else:
                if height[right] >= right_max:
                    right_max= height[right]
                else:
                    water += right_max - height[right]
                right -=1
        return water   '''

        n = len(height)
        prefix = [0]*n
        suffix = [0]*n
        maxi = 0

        for i in range(n):
            if height[i]>maxi:
                prefix[i] = height[i]
                maxi = height[i]
            else:
                prefix[i] = maxi

        maxi = 0
        for i in range(n-1,-1,-1):
            if height[i]>maxi:
                suffix[i] = height[i]
                maxi = height[i]
            else:
                suffix[i] = maxi
        ans = 0
        for i in range(n):
            ans += min(prefix[i],suffix[i])-height[i]
        
        return ans