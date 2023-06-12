class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Convert it to a set
        s = set(nums)
        # best streak
        best = 0
        # find that element whose predecessor doesn't exist and check for its streak
        for i in s:
            # if this number's predecessor doesn't exist
            if i-1 not in s:
                j = i
                # check how long a sequence this has
                best = max(best, j-i+1)
                while j+1 in s:
                    j += 1
                best = max(best, j-i+1)
        return best

s = Solution()
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))