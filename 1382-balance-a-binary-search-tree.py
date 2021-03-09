class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def traverse(node: TreeNode) -> int:
            if node is not None:
                yield from traverse(node.left)
                yield node.val
                yield from traverse(node.right)

        def builder(vals: list[int]) -> TreeNode:
            if not vals:
                return None

            i = len(vals) // 2
            return TreeNode(vals[i], builder(vals[:i]), builder(vals[i + 1:]))

        iterator = traverse(root)
        return builder([val for val in iterator])
