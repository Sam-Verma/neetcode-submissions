class Solution:
    def trap(self, height: List[int]) -> int:
        
        n=len(height)

        prefix=[0]*n
        suffix=[0]*n

        prefix[0]=height[0]
        for i in range(1,n):
            prefix[i] = max(prefix[i-1],height[i])
        
        suffix[n-1]=height[n-1]
        for j in range(n-2,-1,-1):
            suffix[j] = max(height[j],suffix[j+1])
        
        water=0
        for k in range(n):
            water += (min(prefix[k],suffix[k]) - height[k])
        
        return water