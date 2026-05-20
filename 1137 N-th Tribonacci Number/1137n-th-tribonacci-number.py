class Solution:
    def tribonacci(self, n: int,dp={}) -> int:
        """if n >0 and n<3:
            return 1
        
        if n==0:
            return 0
        
        if n in dp:
            return dp[n]
        
        dp[n] = self.tribonacci(n-1,dp)+self.tribonacci(n-2,dp)+self.tribonacci(n-3,dp)

        return dp[n]"""

        if n>0 and n<3:
            return 1
        
        if n == 0:
            return 0
        
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        
        return dp[n]