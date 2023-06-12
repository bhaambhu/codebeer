from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # ignoring the edge case when array is empty for a while

        # assume first element is the minimum
        minx = nums[0]
        # Run an opposite binary search - if middle element is bigger than minx go right, else left
        # Copy the array
        numsCopy = nums
        while len(numsCopy) > 0:
            middleIndex = len(numsCopy) // 2
            middleElement = numsCopy[middleIndex]
            # print(numsCopy, minx, middleIndex, middleElement)
            if middleElement > minx:
                numsCopy = numsCopy[middleIndex + 1 :]
            else:
                minx = middleElement
                numsCopy = numsCopy[:middleIndex]
        return minx


s = Solution()
print(s.findMin(nums=[8,9,10,3,5]))
