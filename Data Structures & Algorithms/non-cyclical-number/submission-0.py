class Solution:
    def isHappy(self, n: int) -> bool:
        
        def number(n):
            total=0
            while n:
                digit = n%10
                total+=digit*digit
                n//=10
            return total
        
        visit=set()
        while n!=1:
            if n in visit:
                return False
            visit.add(n)
            n=number(n)
        return True