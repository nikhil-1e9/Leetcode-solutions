class Solution:
  """
  There is a 1-indexed 8 x 8 chessboard containing 3 pieces.

  You are given 6 integers a, b, c, d, e, and f where:
  
  (a, b) denotes the position of the white rook.
  (c, d) denotes the position of the white bishop.
  (e, f) denotes the position of the black queen.
  Given that you can only move the white pieces, return the minimum number of moves required to capture the black queen.
  
  Note that:
  
  - Rooks can move any number of squares either vertically or horizontally, but cannot jump over other pieces.
  - Bishops can move any number of squares diagonally, but cannot jump over other pieces.
  - A rook or a bishop can capture the queen if it is located in a square that they can move to.
  - The queen does not move.
  """
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        ## Rook takes the queen always in at most 2 moves so the max answer possible is 2
        
        # check if bishop not in between rook and queen
        if a == c == e or b == d == f:
            if (a-c)*(c-e) < 0 or (b-d)*(d-f) < 0:
                return 1
            else: 
                return 2
        # If one of x or y coords of queen coincides with rook's coords then rook takes in 1 move
        if a == e or b == f:
            return 1
        # check If rook not in between bishop and queen
        elif abs(e-c) == abs(f-d):
            if (b-f)*(c-a) == (a-e)*(d-b):
                if (b-f)*(d-b) < 0:
                    return 1
                else: return 2
            else:
                return 1
        return 2
