class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res=[-1]*len(arr)
        maxele=-1
        for i in range(len(arr)-2,-1,-1):
            maxele=max(maxele,arr[i+1])
            res[i]=maxele
        return res