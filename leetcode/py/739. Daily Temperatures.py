from typing import List

class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []  # pair: [temp, index]

    for i, t in enumerate(temperatures):
      while stack and t > stack[-1][0]:
        stackT, stackInd = stack.pop()
        res[stackInd] = i - stackInd
      stack.append((t, i))
    return res
    
  def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
    # a dictionary that holds temperatures not done with
    remaining = {0:temperatures[0]}
    output = [0]*len(temperatures)

    for i in range(len(temperatures)):
      for j in list(remaining):
        if remaining[j]<temperatures[i]:
          output[j] += i-j
          remaining.pop(j)
      remaining[i] = temperatures[i]
    print(remaining)
    return output


s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
