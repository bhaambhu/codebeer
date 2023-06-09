from typing import List
import sb


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # first string be the longest prefix
        res = strs[0]
        # loop through rest and trim as much as we can
        for i in strs:
            for index, letter in enumerate(i):
                try:
                    if res[index] != letter:
                        res = res[0:index]
                except:
                    break
        return res


s = Solution()
print(s.longestCommonPrefix(strs=["flower", "flow", "flight"]))
