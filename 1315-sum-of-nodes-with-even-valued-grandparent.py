class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def sumEven(node: TreeNode, parent: int = 1, grandpa: int = 1) -> int:
            if node is None:
                return 0

            s = 0 if grandpa & 1 else node.val
            s += sumEven(node.left, node.val, parent)
            s += sumEven(node.right, node.val, parent)
            return s

        return sumEven(root)
