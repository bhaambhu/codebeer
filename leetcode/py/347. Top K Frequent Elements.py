import collections

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
      # Create freq map dictionary using Counter
        fdict = collections.Counter(nums)
        return [i for i,v in fdict.most_common(k)]
        
s = Solution()
print(s.topKFrequent([4,1,-1,2,-1,2,3], 2))