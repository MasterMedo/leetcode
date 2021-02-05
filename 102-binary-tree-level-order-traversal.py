from collections import defaultdict


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        def traverse_and_add(root, depth=0):
            nonlocal levels
            if root is None:
                return
            levels[depth].append(root.val)
            traverse_and_add(root.left, depth+1)
            traverse_and_add(root.right, depth+1)

        levels = defaultdict(list)
        traverse_and_add(root)
        return [levels[i] for i in range(len(levels))]
