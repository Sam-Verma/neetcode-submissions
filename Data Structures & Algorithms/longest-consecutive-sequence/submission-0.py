class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset=set(nums)
        max_len=0

        for n in hashset:
            length=1
            if (n-1) not in hashset:
                curr=n
                while curr+1 in hashset:
                    length+=1
                    curr=curr+1
                max_len = max(max_len,length)
        return max_len