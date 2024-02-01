# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  """
  Given the root node of a binary search tree and two integers low and high, 
  return the sum of values of all nodes with a value in the inclusive range [low, high].
  """
  # ---------------------- Simple 3 line recursive solution --------------------
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        return (low <= root.val <= high)*root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

    ## -----------------------Using BST property-----------------------
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: 
            return 0
        
      # If current node value is less than the lowest number in the range,
        # then all left subtree values would be less than this, check only the right subtree
        if root.val < low: 
            return self.rangeSumBST(root.right, low, high)
        
      # If current node value is higher than the highest number in the range,
        # then all right subtree values would be less than this, check only the left subtree
        if root.val > high: 
            return self.rangeSumBST(root.left, low ,high)

      # If node value is in range then include it in answer and 
      # make recursive calls for the left and right subtrees
        if low <= root.val <= high:
            return self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high) + root.val

    ## ----------------- Iterative Level order search ---------------------
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: 
            return 0
        
        BSTsum = 0
        q = [root]
        
        while q:
            node = q.pop()
            
            if low <= node.val <= high:
                BSTsum += node.val
            
            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
        
        return BSTsum
