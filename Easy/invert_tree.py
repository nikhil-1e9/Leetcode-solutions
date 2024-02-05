# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  """
  Given the root of a binary tree, invert the tree, and return its root.
  """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ## Iterative solution O(N) time O(N) space
        if not root:
            return None
        
        q = deque([root])
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return root

    -------------## Recursive ------------------
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        root.left, root.right = root.right, root.left
        
        return root
