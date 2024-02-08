class Solution:
  """
  Given an integer n, return the least number of perfect square numbers that sum to n.

  A perfect square is an integer that is the square of an integer; 
  in other words, it is the product of some integer with itself. 
  For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
  """
  ## ------------ O(n*sqrt(n)) time -------------- ##
    def numSquares(self, n: int) -> int:
        def solve(n):
          # 1(1), 2(1+1), 3(1+1+1)
          if n < 4:
              return n
          
          if n in memo:
              return memo[n]
  
          ans = n
          for i in range(1, int(sqrt(n))+1):
              ans = min(ans, 1 + solve(n-i*i))
          
          memo[n] = ans
          return ans
      
      memo = {}
      return solve(n)


  ##----------------- Mathematical approach O(sqrt(n)) --------------------##
    def numSquares(self, n: int) -> int:
      # Any number can be expressed as sum of upto 4 perfect squares:-
  
      # 1) -> If number is perfect square then answer is 1
  
      # 2) -> If number can be expressed as sum of 2 perfect squares n = i*i + j*j then 
      #       check if n-i*i is perfect square for each i <= sqrt(n)
  
      # 3) -> If number can be expressed as sum of 4 perfect squares then
      #       n = 4^k * (8m+7), check if this criteria is satisfied
  
      # 4) -> If none of the above conditions match the answer would be 3

        root = int(sqrt(n))
        # Check condition 1
        if root * root == n:
            return 1
        
        # Check condition 3
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        
        # Check condition 2
        for i in range(1, int(sqrt(n))+1):
            root = int(sqrt(n-i*i))
            if root * root == n-i*i:
                return 2
          
        # Condition 4
        return 3
