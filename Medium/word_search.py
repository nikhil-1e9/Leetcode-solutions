class Solution:
  """
  Given an m x n grid of characters board and a string word, 
  return true if word exists in the grid.

  The word can be constructed from letters of sequentially adjacent cells, 
  where adjacent cells are horizontally or vertically neighboring. 
  The same letter cell may not be used more than once.
  """
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        length = len(word)

        def search(i, x, y, visited):
            # Word found
            if i == length:
                return True
            # Out of bounds case
            if x < 0 or y < 0 or x >= m or y >= n:
                return False
            # Didn't match at this index
            if board[x][y] != word[i]:
                return False
            # Don't go if already visited
            if (x, y) in visited:
                return False

            res = False
            # Mark current location as visited
            visited.add((x, y))
            # Search up
            res = res or search(i+1, x-1, y, visited)
            # Search down
            res = res or search(i+1, x+1, y, visited)
            # Search left
            res = res or search(i+1, x, y-1, visited)
            # Search right
            res = res or search(i+1, x, y+1, visited)
            # Backtrack and remove current location
            visited.discard((x, y))
        
            return res

        # Search all letters to find if the word can be made starting from that letter
        ans = False
        for i in range(m):
            for j in range(n):
                ans = ans or search(0, i, j, set())
        
        return ans
