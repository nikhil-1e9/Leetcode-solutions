# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  """
  Given the root of a binary tree, return the inorder traversal of its nodes' values.
  """
  # ------------ Recursive ---------------
    def Inorder(self, root, ans):
        if not root:
            return 
        
        self.Inorder(root.left, ans)
        ans.append(root.val)
        self.Inorder(root.right, ans)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.Inorder(root, ans)
        return ans

  # ------------ Iterative ---------------
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                if not stack:
                    return ans
                
                node = stack.pop()
                ans.append(node.val)
                root = node.right
