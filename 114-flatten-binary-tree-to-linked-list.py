class Solution:
    def flatten(self, root: TreeNode) -> None:
        def dfs(node):
            nonlocal prev
            if node is not None:
                if prev is not None:
                    prev.left = None
                    prev.right = node

                right = node.right
                prev = node
                dfs(node.left)
                dfs(right)

        prev = None
        dfs(root)
        return root
