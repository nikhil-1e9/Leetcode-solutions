# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  """
  You are given the root of a binary tree containing digits from 0 to 9 only.

  Each root-to-leaf path in the tree represents a number.
  
  For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
  Return the total sum of all root-to-leaf numbers. 
  Test cases are generated so that the answer will fit in a 32-bit integer.
  
  A leaf node is a node with no children.
  """
    def __init__(self):
        self.ans = 0
      
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def root2Leaf(root, num):
            if not root:
                return
            if not root.left and not root.right:
                num.append(str(root.val))
                self.ans += int("".join(num))
                num.pop()
                return
            
            num.append(str(root.val))
            root2Leaf(root.left, num)
            root2Leaf(root.right, num)
            num.pop()
        
        root2Leaf(root, [])
        return self.ans
