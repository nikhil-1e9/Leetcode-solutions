class Solution:
  """
  You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

  Return the maximum possible length of s.

  A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
  """
    
  ## ----------- Brute force solution -------------
    # Create every possible subsequence from the array and 
    # check the maximum length of the distinct character string
    def createSubseq(self, arr, i, n, ans, out):
        if i == n:
            out.append("".join(ans))
            return

        ans.append(arr[i])
        self.createSubseq(arr, i+1, n, ans, out)
        ans.pop()
        self.createSubseq(arr, i+1, n, ans, out)

    def maxLength(self, arr: List[str]) -> int:
        out = []
        self.createSubseq(arr, 0, len(arr), [], out)
        maxLen = 0
        for string in out:
            if len(set(string)) == len(string):
                maxLen = max(maxLen, len(string))
        return maxLen
