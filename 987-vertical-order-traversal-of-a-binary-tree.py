from collections import defaultdict


class Solution:
    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        def helper(root: TreeNode, x, y, d):
            nonlocal order
            if root is None:
                return

            order[x].append((d, x, root.val))
            helper(root.left, x-1, y-1, d+1)
            helper(root.right, x+1, y-1, d+1)

        order = defaultdict(list)
        helper(root, 0, 0, 0)
        return [list(zip(*sorted(order[y])))[-1] for y in sorted(list(order))]
