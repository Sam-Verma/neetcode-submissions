class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res=[]
        
        def dfs(ip,op):

            if sum(op)==target:
                res.append(op[:])
                return
            
            if not ip or sum(op)>target:
                return

            dfs(ip,op+ip[:1])
            dfs(ip[1:],op)
        
        dfs(nums,[])
        return res
            