class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution: 
    def lowestCommonAncestor(self, root: TreeNode, p:TreeNode, q:TreeNode) ->TreeNode:
        if p.val < root.val and q.val < root.val:
            
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
# Example usage
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)

p = root.left # TreeNode(2)
q = root.left.right # TreeNode(4)
sol = Solution()
lca = sol.lowestCommonAncestor(root, p, q)
print(lca.val)  # Output: 2