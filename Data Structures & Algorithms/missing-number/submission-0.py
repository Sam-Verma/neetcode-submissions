class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n=len(nums)

        total = n*(n+1)//2

        miss=0
        for n in nums:
            miss+=n

        return total-miss