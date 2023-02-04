from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
      # [(10,8)]
        fleets = [(position[i], speed[i]) for i in range(len(position))]
        fleets = sorted(fleets, key=lambda x: x[0], reverse=True)
        stack = []
        for x in fleets:
          # if top's end dest time is less than this element's, don't insert this
          if stack and stack[-1]:
            # time = distance upon speed
            destTimeTop = (target - stack[-1][0])/stack[-1][1]
            destTimeCurrent = (target - x[0])/x[1]
            if destTimeCurrent <= destTimeTop:
              continue
            else:
              stack.append(x)
          else:
            stack.append(x)

        return stack
          

s = Solution()
print(s.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
        