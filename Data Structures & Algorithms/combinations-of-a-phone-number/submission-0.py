class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dic = {"2":'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]

        def backtrack(i,op):
            if len(op)==len(digits):
                res.append(op)
                return
            
            for c in dic[digits[i]]:
                backtrack(i+1,op+c)
            
        if digits:
            backtrack(0,'')
            
        return res
                