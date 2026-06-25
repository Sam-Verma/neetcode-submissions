class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        map={}
        for i,n in enumerate(nums):
            if n in map:
                val=abs(i-map[n])
                if val<=k:
                    return True
            map[n]=i
        return False