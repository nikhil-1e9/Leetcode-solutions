# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  """
  Given the root of a binary search tree, and an integer k, 
  return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
  """
    def inorderTraversal(self, root):
        if not root:
            return 
        
        self.inorderTraversal(root.left)
        arr.append(root.val)
        self.inorderTraversal(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        global arr
        arr = []
        
        self.inorderTraversal(root)

        return arr[k-1]
