from math import inf


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def delete(node: TreeNode) -> TreeNode:
            if node.right is None:
                return node.left

            if node.left is None:
                return node.right

            left = node.left
            root = right = node.right
            while right.left is not None:
                right = right.left

            right.left = left
            return root

        def traverse(node: TreeNode) -> None:
            if node.val > key:
                if node.left is not None:
                    if node.left.val == key:
                        node.left = delete(node.left)
                    else:
                        traverse(node.left)
            else:
                if node.right is not None:
                    if node.right.val == key:
                        node.right = delete(node.right)
                    else:
                        traverse(node.right)

        head = TreeNode(val=inf, left=root)
        traverse(head)
        return head.left
