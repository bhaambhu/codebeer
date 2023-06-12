from typing import List

class Solution:
    def removeElement(self, nums: List[int] = [1], val: int = 3) -> int:
        j = 0
        for i,x in enumerate(nums):
            if nums[i] == val:
                continue
            nums[j] = nums[i]
            j += 1
        return j;

s = Solution()
s.removeElement(nums = [3,2,2,3], val = 3)