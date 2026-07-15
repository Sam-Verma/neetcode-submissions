class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        j,length = len(s)-1,0
        while s[j]==' ':
            j-=1
        while j>=0 and s[j]!=' ':
            length+=1
            j-=1
        return length