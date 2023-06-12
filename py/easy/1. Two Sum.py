class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i,x in enumerate(nums):
            v = nums[i+1:]
            for j,y in enumerate(v):
                print(x,y)
                if x+y == target:
                    print(i,j)
                    return [i,j]

s = Solution()
print(s.twoSum([2,3,7,11,15], 9))
