class Solution:
    def fib(self, n: int,dp={}) -> int:
        if n<=1:
            return n
        if n in dp:
            return dp[n]

        dp[n] = self.fib(n-1,dp) + self.fib(n-2,dp)
        
        return dp[n]