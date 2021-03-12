class Codec:
    def serialize(self, root: TreeNode) -> str:
        def traverse(node: TreeNode) -> None:
            if node is None:
                vals.append('*')
            else:
                vals.append(str(node.val))
                traverse(node.left)
                traverse(node.right)

        vals = []
        traverse(root)
        return ' '.join(vals)

    def deserialize(self, data: str) -> TreeNode:
        def traverse() -> TreeNode:
            if (val := next(iterator, '*')) != '*':
                node = TreeNode(int(val))
                node.left = traverse()
                node.right = traverse()
                return node

        iterator = iter(data.split())
        return traverse()
