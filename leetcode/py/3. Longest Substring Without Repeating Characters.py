class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    l, r = 0, 0
    longest = 0
    # ['a'] 1
    while r < len(s):
      # for i in range(r-l):
      i = 0
      while l+i < r: 
        if s[l+i] == s[r]:
          # if found this character repeating, increment left pointer
          l = l+i+1
        i += 1
      longest = max(longest, r-l+1)
      r += 1
    return longest


s = Solution()
print(s.lengthOfLongestSubstring("abcb"))
