class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num = ''
        for n in digits:
            num+=str(n)
        
        total = int(num)+1

        res = []

        while total:
            digit=total%10
            res.append(digit)
            total//=10
        
        return res[::-1]
            

        