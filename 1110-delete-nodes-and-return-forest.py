class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        def traverse(node: TreeNode, deleted: bool) -> list[TreeNode]:
            children = []
            left = node.left
            left_del = False
            if left is not None:
                if left.val in to_delete:
                    node.left = None
                    left_del = True

                elif deleted:
                    children.append(left)

                children.extend(traverse(left, left_del))

            right = node.right
            right_del = False
            if right is not None:
                if right.val in to_delete:
                    node.right = None
                    right_del = True

                elif deleted:
                    children.append(right)

                children.extend(traverse(right, right_del))

            return children

        to_delete = set(to_delete)
        return traverse(TreeNode(left=root), True) if root is not None else []
