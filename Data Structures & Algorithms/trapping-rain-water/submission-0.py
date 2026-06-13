class Solution:
    def trap(self, height: List[int]) -> int:
        
        res=0
        for i in range(len(height)):

            leftmax = max(height[:i+1])
            rightmax = max(height[i:])

            res+=min(leftmax,rightmax)-height[i]
        return res