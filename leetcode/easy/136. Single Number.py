from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            print(xor, '^', num, ' is ', end="")
            xor ^= num
            print(xor)
        
        return xor

s = Solution()
print(s.singleNumber([0,0,1,2,3]))