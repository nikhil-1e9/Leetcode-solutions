class Solution:
  """
  Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

  The following rules define a valid string:

  Any left parenthesis '(' must have a corresponding right parenthesis ')'.
  Any right parenthesis ')' must have a corresponding left parenthesis '('.
  Left parenthesis '(' must go before the corresponding right parenthesis ')'.
  '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
  """
    def checkValidString(self, s: str) -> bool:
        ## Solution using 2 stacks
        # keep the index of left bracket and star in separate stacks
        # if right breacket comes pop from the left stack else if it is empty
        # pop from the star stack if both are empty return false
        # After processing the string if the index of left bracket is higher than star index
        # then no way to balance the left bracker and return False
        # Otherwise check if left stack is empty and return True

        left_stack, star_stack = [], []
        for i,char in enumerate(s):
            if char == "(":
                left_stack.append(i)
            elif char == '*':
                star_stack.append(i)
            else:
                if not star_stack and not left_stack:
                    return False
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()

        while left_stack and star_stack:
            if left_stack.pop() > star_stack.pop():
                return False

        return not left_stack 
