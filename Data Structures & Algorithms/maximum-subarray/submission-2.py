
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_res=nums[0]
        sum=0

        for j in range(len(nums)):
            if sum<0:
                sum=0
            sum+=nums[j]
            max_res=max(sum,max_res)
        return max_res