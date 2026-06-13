class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        res=0
        i=j=0
        hash_set=set()
        for j in range(n):
            while s[j] in hash_set and i<=j:
                hash_set.remove(s[i])
                i+=1
            hash_set.add(s[j])
            res=max(res,j-i+1)
        return res

            