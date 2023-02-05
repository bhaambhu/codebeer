import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      # We can extend the same approach and use binary search to optimize it
      # min and max limits for bananasPerHour
      l = 1
      r = max(piles)
      minBananasPerHour = r
      while l <= r:
        # if speed is the middle
        bananasPerHour = (l+r)//2
        print("trying speed (", l, ',', r, ') ', bananasPerHour, end=": ")
        # check time taken
        timeTaken = 0
        for x in piles:
          timeTaken += math.ceil(x/bananasPerHour)
        print("time taken = ", timeTaken)
        # take binarySearch decision
        if timeTaken <= h:
          minBananasPerHour = min(minBananasPerHour, bananasPerHour)
          r = bananasPerHour - 1
        else:
          l = bananasPerHour + 1
      return minBananasPerHour
      
    def minEatingSpeedBF(self, piles: List[int], h: int) -> int:
      # Brute force approach
      # max eating speed we need is the max num of bananas in a pile, we have to minimize this
      bananasPerHour = max(piles)
      # At this speed time taken would be number of piles
      timeTaken = len(piles)
      while True:
        timeTaken = 0
        for x in piles:
          timeTaken += math.ceil(x/bananasPerHour)
        if timeTaken <= h:
          bananasPerHour -= 1
        else:
          bananasPerHour += 1
          break
      return bananasPerHour

      

s = Solution()
# print(s.minEatingSpeed(piles = [3,6,7,11], h = 8))
# print(s.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
print(s.minEatingSpeed(piles = [30,11,23,4,20], h = 6))