class Solution:
  """
  Given a signed 32-bit integer x, return x with its digits reversed. 
  If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

  Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
  """
    def reverse(self, x: int) -> int:
        MIN, MAX = -2**31, 2**31
        # Check if number is positive or negative
        pos = True
        if x < 0:
            x *= -1
            pos = False
        
        # Reverse the number
        ans = 0
        while x:
            digit = x % 10
            ans = ans * 10 + digit
            x //= 10
        
        # Make number negative if it was negative initially
        ans = ans if pos else -ans

        # Check if ans out of accepted range
        if ans < MIN or ans >= MAX:
            ans = 0
        
        return ans
