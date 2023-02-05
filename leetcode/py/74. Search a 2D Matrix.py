from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      rows = len(matrix)
      cols = len(matrix[0])
      items = rows*cols
      l = 0
      r = items
      while l <= r:
        middleIndex = (l+r) // 2
        # print('getting elemAt ', middleIndex, end=" i.e. (")
        rowIndex = middleIndex // cols
        colIndex = middleIndex % cols
        if rowIndex >= rows or colIndex >= cols:
          return False
        # print(rowIndex, ',', colIndex, ") its ", end="")
        val = matrix[rowIndex][colIndex]
        # print(val)
        if val > target:
          r = middleIndex - 1
          # print('new r ', r)
        elif val < target:
          l = middleIndex + 1
          # print('new l ', l)
        else:
          return True
      return False

s = Solution()
print(s.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3))
# print(s.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=13))
# print(s.searchMatrix(matrix=[[1]], target=2))