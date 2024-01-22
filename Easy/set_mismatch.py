class Solution:
  """
  You have a set of integers s, which originally contains all the numbers from 1 to n. 
  Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, 
  which results in repetition of one number and loss of another number.

  You are given an integer array nums representing the data status of this set after the error.
  Find the number that occurs twice and the number that is missing and return them in the form of an array.
  """
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ## --------- Solution using set ---------
        n = len(nums)
        s = set(nums)
        
        repeat = sum(nums) - sum(s)
        miss = n*(n+1)//2 - sum(s)
        
        return [repeat, miss]


    def findErrorNums(self, nums: List[int]) -> List[int]:
        ## -------------- Solution using sum and sum of squares of first n numbers ------------
        n = len(nums)
        S = n*(n+1)//2
        S2 = n*(n+1)*(2*n+1)//6
        SUM = sum(nums)
        SUM2 = sum(x*x for x in nums)
        diff = SUM - S
        diff2 = SUM2 -S2
        
        rep = (diff2+diff**2)//(2*diff)
        miss = (diff2-diff**2)//(2*diff)
      
        return [rep, miss]
