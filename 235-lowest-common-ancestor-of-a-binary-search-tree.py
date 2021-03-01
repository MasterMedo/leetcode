class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def traverse(node: TreeNode):
            if node is not None:
                found = node in (p, q)
                found_left = traverse(node.left)
                found_right = traverse(node.right)
                if found and (found_left or found_right):
                    return node

                if found_left and found_right:
                    return node

                return found or found_left or found_right

        return traverse(root)
