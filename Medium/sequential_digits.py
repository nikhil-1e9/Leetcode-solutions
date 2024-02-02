class Solution:
  """
  An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

  Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
  """
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = ['1','2','3','4','5','6','7','8','9']
        low = str(low)
        high = str(high)

        ans = []
        x = len(low)
        flag = 0
        
        while True:
            for i in range(10-x):
                num = int("".join(digits[i:i+x]))
                if num < int(low):
                    continue
                
                if num <= int(high) and num >= int(low):
                    ans.append(num)
                else:
                    flag = 1
                    break
            
            x += 1
            
            if flag or x == 10 : 
              break
        
        return ans

    
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        out = []
        q = deque(range(1,10))
        
        while q:
            num = q.popleft()
            if low <= num <= high:
                out.append(num)
            
            last = num % 10
            
            if last < 9: 
              queue.append(num*10 + last + 1)
                    
        return out
