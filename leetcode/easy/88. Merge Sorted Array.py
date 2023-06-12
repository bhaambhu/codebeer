from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Loop backwards from last to first
        index = m+n-1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[index] = nums1[m]
                m -= 1
            else:
                nums1[index] = nums2[n]
                n -= 1
            index -= 1
        # Copy all remaining items
        while m >= 0:
            nums1[index] = nums1[m]
            m -= 1
            index -= 1
        while n >= 0:
            nums1[index] = nums2[n]
            n -= 1
            index -= 1
        print(m,n,nums1)
        

s = Solution()
s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
s.merge(nums1 = [1], m = 1, nums2 = [], n = 0)
s.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

