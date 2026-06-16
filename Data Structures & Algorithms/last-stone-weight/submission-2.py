import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap=[-n for n in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            x=-heapq.heappop(heap)
            y=-heapq.heappop(heap)

            n=abs(x-y)
            if n>0:
                heapq.heappush(heap,-n)
        
        return abs(heap[0]) if len(heap)>0 else 0