class Solution:
    def climbStairs(self, n: int) -> int:

        dp=[-1]*(n+1)

        def dfs(i):
            if i<=2:
                return i

            if dp[i]!=-1:
                return dp[i]
            
            dp[i]=dfs(i-1)+dfs(i-2)
            return dp[i]

        return dfs(n)