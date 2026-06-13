class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def solve(ip,op):
            if len(ip) == 0:
                res.append(op)
                return
            # op1=op
            # op2=op+ip[:1]
            solve(ip[1:],op)
            solve(ip[1:],op+ip[:1])
            return
        
        solve(nums,list())
        return res