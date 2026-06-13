from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        cnt = [0]*26
        for i in range(len(s)):
            cnt[ord(s[i])-ord('a')]+=1
            cnt[ord(t[i])-ord('a')]-=1
        
        for count in cnt:
            if count!=0:
                return False
        return True