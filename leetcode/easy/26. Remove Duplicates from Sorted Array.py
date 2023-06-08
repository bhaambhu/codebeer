from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    i,j = 0,1
    if len(nums) < 1:
      return 0
    while j < len(nums):
      while (j < len(nums)) and (nums[j] == nums[i]):
        nums[j] = None
        j += 1
      # we arrive at a different number finally
      if j < len(nums):
        nums[i+1] = nums[j]
        i += 1
        if i == j:
          j += 1
    print(nums)
    return i+1

s = Solution()
# print(s.removeDuplicates(nums=[]))
# print(s.removeDuplicates(nums=[1,2,3]))
print(s.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))