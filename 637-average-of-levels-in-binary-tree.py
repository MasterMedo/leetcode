from collections import defaultdict


class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        def traverse_and_add(root, depth=0):
            nonlocal levels
            if root is None:
                return

            levels[depth][0] += root.val
            levels[depth][1] += 1
            traverse_and_add(root.left, depth + 1)
            traverse_and_add(root.right, depth + 1)

        levels = defaultdict(lambda: [0, 0])
        traverse_and_add(root)
        return [levels[i][0] / levels[i][1] for i in range(len(levels))]
