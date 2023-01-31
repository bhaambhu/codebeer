from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

S = Solution()
print(S.containsDuplicate([1, 2, 3]))
print(S.containsDuplicate([1, 2, 3, 2]))
