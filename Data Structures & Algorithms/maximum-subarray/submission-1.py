
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_res=-1
        sum=nums[0]
        i=0
        for j in range(1,len(nums)):
            if sum<=0:
                i=j
                sum=0
            sum+=nums[j]
            max_res=max(sum,max_res)
        return max(max_res,sum)