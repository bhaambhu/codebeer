class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = []
        groupDict = {}
        for i,x in enumerate(strs):
            oneString = list(x)
            oneString.sort()
            oneString = "".join(oneString)
            groupDict.setdefault(oneString, []).append(x)
        for v in groupDict.values():
          groups.append(v)
        print(groups)
            
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))