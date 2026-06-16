import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = collections.Counter(nums)
        heap = []

        for key,cnt in count.items():
            heapq.heappush(heap,(cnt,key))

            if len(heap)>k:
                heapq.heappop(heap)
        
        return [num for cnt,num in heap]
         