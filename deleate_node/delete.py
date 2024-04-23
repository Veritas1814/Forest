class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root,key: int):
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            root.val = self.for_right(root.right).val
            root.right = self.deleteNode(root.right, root.val)
        return root
    def for_right(self,node):
        current = node
        while current.left:
            current = current.left
        return current
c1=Solution()
a=TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(6,None,TreeNode(7)))
c1.deleteNode(a,3)

