class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        count=collections.Counter(s1)
        need=len(count)
        have=0

        for i in range(len(s1)):
            if s2[i] in count:
                count[s2[i]]-=1
                if count[s2[i]]==0:
                    have+=1

        if have==need:
            return True
        
        l=0
        for r in range(len(s1),len(s2)):

            char = s2[r]
            if char in count:
                count[char]-=1
                if count[char]==0:
                    have+=1
            
            left = s2[l]
            if left in count:
                if count[left]==0:
                    have-=1
                count[left]+=1

            l+=1
            if have==need:
                return True
        
        return False



