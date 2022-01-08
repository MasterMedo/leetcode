from math import inf


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def traverse(node: TreeNode) -> None:
            if node is None:
                return [inf, inf]

            if node.val == x:
                return [1, inf]

            if node.val == y:
                return [inf, 1]

            level_x1, level_y1 = traverse(node.left)
            level_x2, level_y2 = traverse(node.right)
            level_x = min(level_x1, level_x2)
            level_y = min(level_y1, level_y2)
            if level_x == level_y and level_x == 1:
                return [inf, inf]

            return [level_x + 1, level_y + 1]

        level_x, level_y = traverse(root)
        return level_x == level_y and level_x not in [inf, 1]
