class Solution:
  """
  
  """
  ## ---------- Brute Force -> O(n^2*logn) time, O(1) space----------- ##
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = len(s1)
        for i in range(len(s2)-l+1):
            if sorted(s2[i:i+l]) == sorted(s1):
                return True
        return False

  ## ---------- Optimal approach -> O(n) time, O(n) space ---------- ##
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = len(s1)
        perm1 = [0]*26
        perm2 = [0]*26
        
        for x in range(l):
            idx1 = ord(s1[x])-ord('a')
            idx2 = ord(s2[x])-ord('a')
            perm1[idx1] += 1
            perm2[idx2] += 1

        if perm1 == perm2:
            return True

        i, j = 1, l
        while j < len(s2):
            out = ord(s2[i-1])-ord('a')
            _in = ord(s2[j])-ord('a')
            
            perm2[out] -= 1
            perm2[_in] += 1
            
            i += 1
            j += 1

            if perm1 == perm2:
                return True
        
        return False
