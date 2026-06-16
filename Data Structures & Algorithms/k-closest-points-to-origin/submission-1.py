class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap=[]
        res=[]
    
        for point in points:
            distance = math.dist(point,[0,0])
            heap.append([distance,point])
        heapq.heapify(heap)
        while k>0:
            dis,point = heapq.heappop(heap)
            res.append(point)
            k-=1
        
        return res