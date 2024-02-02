class Solution:
  """
  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

  - Each row must contain the digits 1-9 without repetition.
  - Each column must contain the digits 1-9 without repetition.
  - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
  
  Note:
  
  A Sudoku board (partially filled) could be valid but is not necessarily solvable.
  Only the filled cells need to be validated according to the mentioned rules.
  """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      # Function to check valid rows and cols
        def validRow(row):
            seen = set()
            
            for val in row:
                if val == '.':
                    continue
                
                if val not in seen:
                    seen.add(val)
                else: 
                    return False
            
            return True

      # Function to check valid 3x3 grid
        def validGrid(startRow, startCol):
            seen = set()
            
            for i in range(startRow, startRow+3):
                for j in range(startCol, startCol+3):
                    val = board[i][j]
                    
                    if val == '.':
                        continue
                    
                    if val not in seen:
                        seen.add(val)
                    else: 
                        return False
            
            return True

      # Check if all rows are valid
        for row in board:
            if not validRow(row):
                return False

      # Check if all columns are valid
        for col in zip(*board):
            if not validRow(col):
                return False

      # Check if all 3x3 grids are valid
        for row in range(0,9,3):
            for col in range(0,9,3):
                if not validGrid(row, col):
                    return False
        
        return True
