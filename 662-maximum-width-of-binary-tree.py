class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        def traverse(node: TreeNode, depth: int, i: int) -> None:
            nonlocal levels

            if node is None:
                return

            if depth >= len(levels):
                levels.append([i, i])

            levels[depth][1] = i
            traverse(node.left, depth + 1, i << 1)
            traverse(node.right, depth + 1, (i << 1) | 1)

        levels = []
        traverse(root, 0, 0)
        return max(hi - lo + 1 for lo, hi in levels)
