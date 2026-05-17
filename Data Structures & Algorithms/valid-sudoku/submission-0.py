class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(len(board))]
        columns = [set() for i in range(len(board[0]))]
        quads = [[set() for j in range(3)]for i in range(3)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in columns[j]:
                    return False
                else:
                    rows[i].add(board[i][j])
                    columns[j].add(board[i][j])
                
                x, y = i // 3, j // 3
                if board[i][j] in quads[x][y]:
                    return False
                else:
                    quads[x][y].add(board[i][j])
        return True