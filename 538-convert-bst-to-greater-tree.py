class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def helper(node: TreeNode, greater=0) -> int:
            if node is None:
                return 0

            node.val += helper(node.right, greater) + greater
            return node.val + helper(node.left, node.val) - greater

        helper(root)
        return root
