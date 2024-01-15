class Solution:
  """
  You are given two 0-indexed integer arrays nums1 and nums2 of even length n.
  You must remove n / 2 elements from nums1 and n / 2 elements from nums2. After the removals, you insert the remaining elements of nums1 and nums2 into a set s.
  Return the maximum possible size of the set s.
  """
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        # Select distinct elements of A which are not in B and vice-versa
        # if the number of total distinct elements in any exceeds n/2 then take minimum of two
        ## min( n(A-B), n/2 ) + min( n(B-A), n/2 )
        # If the total above exceeds n then answer is n, else if the total is less than n 
        # then also add the common elements from both sets
        
        ## FINAL ANS = min ( n, min( n(A-B), n/2 ) + min( n(B-A), n/2 ) + n(A ∩ B) )
        
        set1 = set(nums1)
        set2 = set(nums2)
        A_minus_B = set1.difference(set2)
        B_minus_A = set2.difference(set1)
        x1 = min(len(A_minus_B), len(nums1)//2)
        x2 = min(len(B_minus_A), len(nums2)//2)
        A_intersection_B = set1.intersection(set2)
        x3 = len(A_intersection_B)
        
        ans = min(len(nums1), x1+x2+x3)
        return ans
