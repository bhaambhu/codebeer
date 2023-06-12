from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

S = Solution()
print(S.containsDuplicate([1, 2, 3]))
print(S.containsDuplicate([1, 2, 3, 2]))
