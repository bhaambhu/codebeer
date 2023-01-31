# Okay now there could be any number of solutions if you think of using string join() then split() and try use skip escape characters, then try to escape already present escape characters, double escape characters and so on... but none of that matters as we have been given a list of strings, so we can take advantage of that as follows:
# every string in that list has some length, join them into a string but add <lengthOfString># before each string. This is a bulletproof solution that doesnt need to escape any characters in the original string because by doing this the encoded string will begin with a number and # character, telling us the length of first substring, we can then chop it off and all special and escape characters that were in that substring dont need to be dealt with. Now the chopped string will again begin with a number and # telling us length of next substring and so on. 
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for i in strs:
          res += str(len(i)) + "#" + i
        return (res)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # Loop for every character in the string
        pointer = 0
        locationOfHash = 0
        res = []
        while pointer < len(str) - 1:
          while str[locationOfHash] != "#":
            locationOfHash += 1
          # At this point we've reached locationOfHash
          lengthOfSubstring = int(str[pointer:locationOfHash])
          # Add this substring to list
          res.append(str[locationOfHash+1: locationOfHash+1+lengthOfSubstring])
          # Move the pointers forward
          pointer = locationOfHash+1+lengthOfSubstring
          locationOfHash = pointer+1
        return res

s = Solution()
print(s.decode(s.encode(["we", "say3", ":", "yes"])))