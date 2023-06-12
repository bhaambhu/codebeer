class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # What we have to do is,
        # For every ith element we have to calculate
        # Prefix product: i.e. 0th * 1th * ... * (i-1)th index element
        # and multiply this with the
        # Postfix product: i.e. (i+1)th * (i+2)th * ... * (n-1)th index element
        # Since we have to do it for every element, we can do it in single pass i.e. O(n)

        preProduct, postProduct = 1,1
        resultArr = [1] * len(nums)
        lastIndex = len(nums) - 1
        for i,x in enumerate(nums):
            resultArr[i] *= preProduct
            preProduct *= x
            resultArr[lastIndex - i] *= postProduct
            postProduct *= nums[lastIndex - i]
        return resultArr

s = Solution()
print(s.productExceptSelf([1,2,3,4]))