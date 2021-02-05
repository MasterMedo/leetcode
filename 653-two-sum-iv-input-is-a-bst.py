class Solution:
    def findTarget(self, root: TreeNode, target: int) -> bool:
        def traverse(node: TreeNode) -> bool:
            nonlocal values

            if node is None:
                return False

            if node.val in values:
                return True

            values.add(target - node.val)
            return traverse(node.left) | traverse(node.right)

        values = set()
        return traverse(root)
