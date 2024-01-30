class Solution:
  """
  You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

  Evaluate the expression. Return an integer that represents the value of the expression.
  
  Note that:
  
  - The valid operators are '+', '-', '*', and '/'.
  - Each operand may be an integer or another expression.
  - The division between two integers always truncates toward zero.
  - There will not be any division by zero.
  - The input represents a valid arithmetic expression in a reverse polish notation.
  - The answer and all the intermediate calculations can be represented in a 32-bit integer.
  """
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for char in tokens:
            if char not in ('+','-','*','/'):
                stack.append(int(char))
            
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                
                if char == '+':
                    stack.append(num2 + num1)
                
                elif char == '-':
                    stack.append(num2 - num1)
                
                elif char == '*':
                    stack.append(num2 * num1)
                
                else:
                    stack.append(int(float(num2 / num1)))
        
        return stack[-1]
