class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        car = sorted(zip(position,speed))

        stack=[]

        for pos,speed in reversed(car):
            time = (target-pos)/speed
            stack.append(time)
            
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)

