class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        merged=[intervals[0]]
        for curr in intervals:
            prev=merged[-1]
            if prev[1]>=curr[0]:
                prev[1]=max(prev[1],curr[1])
            else:
                merged.append(curr)
        return merged
