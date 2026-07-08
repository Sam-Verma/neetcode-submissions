class Solution:
    def climbStairs(self, n: int) -> int:

        # dp=[0]*n
        # def dfs(i):
        #     if i<=0:
        #         return dp[0]

        #     if dp[i]!=0:
        #         return dp[i]
            
        #     dp[i]=dfs(i-1)+dfs(i-2)
        
        # dfs(n)
        # return 

        if n<=2:
            return n
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2

        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        
        return dp[-1]