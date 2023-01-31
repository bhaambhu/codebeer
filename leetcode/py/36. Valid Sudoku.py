import collections
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Lets create lists, one for each 3x3, each col, and each row
        listsOfSetsOfCols = collections.defaultdict(set)
        listsOfSetsOfRows = collections.defaultdict(set)
        listsOfSetsOf3x3s = collections.defaultdict(set)
        brandnew = collections.defaultdict(set)
        # listsOfSetsOfCols = [set() for _ in range(9)]
        # listsOfSetsOfRows = [set() for _ in range(9)]
        # listsOfSetsOf3x3s = [set() for _ in range(9)]
        # One loop to rule them all
        for i,currentRow in enumerate(board):
            for j,item in enumerate(currentRow):
                if(item!="."):
                    item = int(item)
                    sizeColBefore = len(listsOfSetsOfCols[j])
                    listsOfSetsOfCols[j].add(item)
                    if(len(listsOfSetsOfCols[j]) == sizeColBefore):
                      return False
                    sizeRowBefore = len(listsOfSetsOfRows[i])
                    listsOfSetsOfRows[i].add(item)
                    if(len(listsOfSetsOfRows[i]) == sizeRowBefore):
                      return False
                    # The index of this one is 3*i + j where i and j must be ints casted after division of i and j by 3
                    cid = 3*(int(i/3)) + int(j/3)
                    print("for i=", i, " j=", j, ' its (', i//3, ',', j//3, ') cid is ',cid)
                    brandnew[(i//3, j//3)].add(item)
                    # print("inserting at ", cid, "th 3x3 cube")
                    size3x3SetBefore = len(listsOfSetsOf3x3s[cid])
                    listsOfSetsOf3x3s[cid].add(item)
                    if(len(listsOfSetsOf3x3s[cid]) == size3x3SetBefore):
                      return False
        print(brandnew)
        # lets try accessing through pairs
        print("tuple access", listsOfSetsOf3x3s[(0,0)])
        return True        

s = Solution()
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
# print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]))