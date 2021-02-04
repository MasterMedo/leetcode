from heapq import merge


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        def inorder(root):
            if root is None:
                return []

            return inorder(root.left) + [root.val] + inorder(root.right)

        return merge(inorder(root1), inorder(root2))
