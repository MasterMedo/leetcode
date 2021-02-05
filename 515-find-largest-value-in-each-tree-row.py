from collections import defaultdict
from math import inf


class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:
        def traverse(node, depth=0):
            nonlocal depths

            if node is None:
                return

            depths[depth] = max(depths[depth], node.val)
            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)

        depths = defaultdict(lambda: -inf)
        traverse(root)
        return [depths[i] for i in range(len(depths))]
