class Solution:
  """
  Given a positive integer n, find the pivot integer x such that:

  - The sum of all elements between 1 and x inclusively 
    equals the sum of all elements between x and n inclusively.
  
  Return the pivot integer x. If no such integer exists, return -1. 
  It is guaranteed that there will be at most one pivot index for the given input.
  """
  ## ----------- O(n) time ---------- ##
    def pivotInteger(self, n: int) -> int:
        total = n*(n+1)//2
        leftSum = 0
        
        for x in range(1, n+1):
            leftSum += x
            rightSum = total - x*(x-1)//2

            if leftSum == rightSum:
                return x
        
        return -1

  ## ------- Binary Search -> O(logn) time ------- ##
    def pivotInteger(self, n: int) -> int:
        total = n * (n+1) // 2
        left, right = 1, n
        pivot = -1

        while left <= right:
            mid = left + (right-left) // 2
            leftSum = mid * (mid+1) // 2
            rightSum = total - mid * (mid-1) // 2

            if leftSum > rightSum:
                right = mid - 1
            elif leftSum < rightSum:
                left = mid + 1
            else:
                pivot = mid
                break
        
        return pivot


  ## ------- Square root O(1) (constant time) ------- ##
    def pivotInteger(self, n: int) -> int:
        ## LeftSum   =   RightSum
        ## x*(x+1)/2 = n*(n+1)/2 - x*(x-1)/2
        ## => x = sqrt(n*(n+1)/2)
        ## but x must be an integer
        ## the answer boils down to check the condition if x is an integer

        sqrt = (n*(n+1)//2)**0.5
        
        if int(sqrt) == sqrt:
            return int(sqrt)
        return -1
