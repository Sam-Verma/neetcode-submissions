class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        cnt={}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in cnt:
                return [cnt[diff],i]
            cnt[n]=i
            