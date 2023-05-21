from typing import List


class Solution:
    def diagonalSum(self, mat: List[int]) -> int:
        n = len(mat[0])
        s = 0
        for i, j in enumerate(mat):
            s = s + j[i] + j[n-i-1]
        # If n is odd, subtract center number because it has been added twice
        if n % 2 != 0:
            s = s - mat[(n-1)//2][(n-1)//2]
        return s


s = Solution()
# [[1,2,3],[4,5,6],[7,8,9]]
# [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
# [[5]]
print(s.diagonalSum(
    mat=[[1,2,3],[4,5,6],[7,8,9]]))
