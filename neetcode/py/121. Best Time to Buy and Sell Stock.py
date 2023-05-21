from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Add all profits in this and return the maximum
        profits = []
        lastNumber = prices[0]
        localProfit = 0
        for i, x in enumerate(prices):
            # If next number is greater then previous number, continue adding
            # else reset
            if x <= lastNumber:
                profits.append(localProfit)
                localProfit = 0
                lastNumber = x
            else:
                localProfit = max(localProfit, x - lastNumber)
        profits.append(localProfit)
        return max(profits)


s = Solution()
print(s.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(s.maxProfit(prices=[7, 6,4,3,1]))
