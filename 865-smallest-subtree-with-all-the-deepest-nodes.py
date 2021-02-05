class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def traverse(node: TreeNode) -> int:
            if node is None:
                return node, 0

            left, ldepth = traverse(node.left)
            right, rdepth = traverse(node.right)

            if ldepth == rdepth:
                return node, ldepth + 1
            elif ldepth > rdepth:
                return left, ldepth + 1
            else:
                return right, rdepth + 1

        return traverse(root)[0]
