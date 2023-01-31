from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = position.copy()
        print(fleets)
        # loop until there's only one fleet remaining
        while len(fleets) > 1:
          # calculate the timestep
          timeStep = 1/max(speed)
          print('after time ', timeStep)
          # lets see where everyone is after one timestep
          newFleets = list()
          newSpeeds = list()
          for i,x in enumerate(fleets):
            # if any fleet reached target, remove it
            if x >= target:
              timeStep = 1/max(speed)
            else:
              
            fleets[i] += timeStep * speed[i]
            # adjust speeds of equal position cars to make them fleet
            for j,y in enumerate(fleets):
              if x == y:
                fleets.pop(j)
                speed.pop(j)
                print(fleets)
                timeStep = 1/max(speed)
          print(fleets)
          

s = Solution()
print(s.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
        