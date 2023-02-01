class Solution:
  def romanToInt(self, s: str) -> int:
    res = 0
    i = 0
    while i < len(s): #IVV
      if s[i] == "I":
        if (i < len(s) -1) and s[i+1] == "V":
          res += 4
          i += 1
        elif (i < len(s) -1) and s[i+1] == "X":
          res += 9
          i += 1
        else:
          res += 1
      elif s[i] == "X":
        if (i < len(s) -1) and s[i+1] == "L":
          res += 40
          i += 1
        elif (i < len(s) -1) and s[i+1] == "C":
          res += 90
          i += 1
        else:
          res += 10
      elif s[i] == "C":
        if (i < len(s) -1) and s[i+1] == "D":
          res += 400
          i += 1
        elif (i < len(s) -1) and s[i+1] == "M":
          res += 900
          i += 1
        else:
          res += 100
      elif s[i] == "V":
        res += 5
      elif s[i] == "L":
        res += 50
      elif s[i] == "D":
        res += 500
      elif s[i] == "M":
        res += 1000
      i += 1
    return res
      

s = Solution()
print(s.romanToInt("XX") + s.romanToInt("L"))
