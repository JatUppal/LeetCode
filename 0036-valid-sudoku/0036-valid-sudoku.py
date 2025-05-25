class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != ".":
                    boxNum = (((row // 3) * 3) + (col // 3 + 1))
                    if(("row" + str(row), board[row][col]) in seen or ("col" + str(col), board[row][col]) in seen or ("box" + str (boxNum), board[row][col]) in seen):
                        return False
                    else:
                        seen.add(("row" + str(row), board[row][col]))
                        seen.add(("col" + str(col), board[row][col]))
                        seen.add(("box" + str(boxNum), board[row][col]))
        return True