class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans = True
        mp = {
            0:set(),
            1:set(),
            2:set(),
            3:set(),
            4:set(),
            5:set(),
            6:set(),
            7:set(),
            8:set(),

        }

        

        for i in range(9):
            row =set()
            
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in mp[j]:
                        return False
                    else:
                        mp[j].add(board[i][j])
                        
                    if board[i][j] in  row:
                        return False
                    else:
                        print(row)
                        row.add(board[i][j])

                if i%3==0 and j%3==0:
                    
                    checker = set()
                    # Print the top-left value of each 3x3 subgrid
                    for l in range(i, i+3):
                        for k in range(j, j+3):
                            if board[l][k] != "." and board[l][k] in checker:
                                return False
                            elif board[l][k] != ".":
                                checker.add(board[l][k])
            
            

        

        return True