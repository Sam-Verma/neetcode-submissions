class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        res=[]
        sorted_dict = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        for key,value in sorted_dict.items():
            if k>0:
                res.append(key)
                k-=1
        return res