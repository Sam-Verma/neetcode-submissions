class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hash = set(nums)
        res=0

        for n in hash:
            cnt=1
            curr=n
            while (curr+1) in hash:
                cnt+=1
                curr+=1
            res=max(res,cnt)
        return res

        