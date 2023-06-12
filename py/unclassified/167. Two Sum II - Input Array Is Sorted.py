from bisect import bisect_left
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      l, r = 0, len(numbers) - 1
      while l < r:
          countSum = numbers[l] + numbers[r]

          if countSum > target:
              r -= 1
          elif countSum < target:
              l += 1
          else: 
              return [l + 1, r + 1]
    def twoSumUsingBinarySearch(self, numbers: List[int], target: int) -> List[int]:
        lastIndex = len(numbers) - 1
        l = 0
        # Since list is sorted we can use binary search
        while l < lastIndex:
            itemToFind = target - numbers[l]
            # Attempt to Find item using binary search
            r = bisect_left(numbers[l+1:], itemToFind)
            if r != len(numbers) and numbers[l+1:][r] == itemToFind:
                print("found l ", l, " r ", r)
                return [l+1, r+l+2]
            else:
                print("incrementing")
                l += 1

s = Solution()
print(s.twoSum([2,7,9,10], 9))