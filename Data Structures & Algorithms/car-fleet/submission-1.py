class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        car = list(zip(position,speed))
        car.sort()

        fleet=0
        lasttime=0

        for pos,speed in reversed(car):
            time = (target-pos)/speed
            if time>lasttime:
                fleet+=1
                lasttime=time

        return fleet

