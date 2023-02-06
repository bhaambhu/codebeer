from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    mp = 0
    i = 1
    while i < len(prices):
      if prices[i] > prices[i-1]:
        mp += prices[i] - prices[i-1]
      i += 1
    return mp

s = Solution()
# print(s.maxProfit(prices=[7,1,5,3,6,4]))
# print(s.maxProfit(prices=[1,2,3]))
print(s.maxProfit(prices=[0,1]))