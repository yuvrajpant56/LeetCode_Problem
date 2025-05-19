class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool: 
        def is_valid(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (is_valid(node.left, low, node.val) and
                    is_valid(node.right, node.val, high))
        return is_valid(root)
    
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(7)

sol = Solution()
print(sol.isValidBST(root))
