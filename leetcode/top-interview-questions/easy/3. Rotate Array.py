from typing import List
# TODO: Complete this
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
          return nums
        k = k % len(nums)
        print('new k=', k)
        newArr = [0]*len(nums)
        for c in range(len(nums)):
          newArr[c] = nums[c-k]
        nums = newArr.copy()
        return nums

    def rotateO1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l < 1:
          return
        t2 = nums[0]
        i = k
        # move pointer circularly
        if i >= l:
          i = i - l
        # loop once for every element of nums array
        print("given: ", nums)
        for c in range(l):
          print('swap ', nums[i], ' with ', t2, end=' :')
          # store this number in temporary variable
          t1 = nums[i]
          # swap this number with correct number
          nums[i] = t2
          # store the number we picked up
          t2 = t1
          # move the pointer k positions ahead, circularly
          
          i += k
          if i >= l:
            i -= l
          print(nums)
        # t2 = nums[1]
        # i = k+1
        # for c in range(l//2):
        #   print('swap ', nums[i], ' with ', t2, end=' :')
        #   # store this number in temporary variable
        #   t1 = nums[i]
        #   # swap this number with correct number
        #   nums[i] = t2
        #   # store the number we picked up
        #   t2 = t1
        #   # move the pointer k positions ahead, circularly
        #   i += k
        #   if i >= l:
        #     i -= l
        #   print(nums)
        print(nums)



s = Solution()
# print(s.rotate(nums=[1,2,3,4,5,6,7,8], k = 3))
# print(s.rotate(nums=[-1,-100,3,99], k = 2))
# print(s.rotate(nums=[1,2,3,4,5,6,7], k = 3))
print(s.rotate(nums=[1,2,3], k = 16))
# print(s.rotate(nums=[1,2,3], k = 1))
# print(s.rotateO1(nums=[1,2,3,4,5,6], k = 5))