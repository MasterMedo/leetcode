from math import inf


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def helper(node, maxSoFar, minSoFar):
            if node is not None:
                lo = abs(maxSoFar - node.val)
                hi = abs(minSoFar - node.val)
                minSoFar = min(minSoFar, node.val)
                maxSoFar = max(maxSoFar, node.val)
                return max(lo, hi,
                           helper(node.left, maxSoFar, minSoFar),
                           helper(node.right, maxSoFar, minSoFar))
            return -inf

        return max(helper(root.left, root.val, root.val),
                   helper(root.right, root.val, root.val))
