class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        node = root
        candidate = TreeNode(-float("inf"))
        candidates = []
        while node:
            if node.left is not None:
                prev = node.left
                while prev.right is not None and prev.right != node:
                    prev = prev.right

                if prev.right is None:
                    prev.right = node
                    node = node.left
                else:  # prev.right == node
                    prev.right = None
                    if node.val < candidate.val:
                        candidates += [candidate, node]
                    candidate = node
                    node = node.right
            else:
                if node.val < candidate.val:
                    candidates += [candidate, node]

                candidate = node
                node = node.right

        first = candidates[0]
        last = candidates[-1]
        first.val, last.val = last.val, first.val
