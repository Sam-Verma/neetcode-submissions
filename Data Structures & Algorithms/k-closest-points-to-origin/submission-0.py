class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap=[]
        res=[]
    
        for point in points:
            distance = math.dist(point,[0,0])
            heapq.heappush(heap,[distance,point])
        
        while k>0:
            dis,point = heapq.heappop(heap)
            res.append(point)
            k-=1
        
        return res