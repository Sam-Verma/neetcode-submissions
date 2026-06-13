class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=nums[0]
        count=1
        for n in nums:
            if count==0:
                maj=n
            if n==maj:
                count+=1
            else:
                count-=1

        return maj