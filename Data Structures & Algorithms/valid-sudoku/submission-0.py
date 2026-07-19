class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        flag = (self.row_duplicate_validation(board) and self.col_duplicate_validation(board) and
                 self.matrix_three_cross_three_check(board)
                 )

        # flag = self.col_duplicate_validation(board)
        return flag
    
        


    def row_duplicate_validation(self,board):
        for row in range(len(board)):
            each_row = board[row]
            
            

            each_row = [row for row in each_row if row !='.']

            duplication_check = list(set(each_row))
            


            if len(duplication_check) != len(each_row):
                return False 
        return True 
    

    def col_duplicate_validation(self,board):
        rows  = len(board)
        cols = len(board[0])


        for col in range(cols):
            arr = [] 
            for row in range(rows):
                arr.append(board[row][col])


            arr = [col for col in arr if col!='.']
            # print(arr)
            
            duplication_check = list(set(arr))
            # print(duplication_check)

            
            
            if len(duplication_check)!=len(arr):
                # print(duplication_check,arr)
                return False 
        return True 
    

    def matrix_three_cross_three_check(self, board):
        rows = len(board)
        cols = len(board[0])

        for start_row in range(0, rows, 3):
            for start_col in range(0, cols, 3):

                values = []

                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        if board[row][col] != ".":
                            values.append(board[row][col])

                if len(values) != len(set(values)):
                    return False

        return True
    