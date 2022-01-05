class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        def traverse(root):
            nonlocal data
            if root is None:
                return None

            data[root.val] = traverse(root.left), traverse(root.right)
            return root.val

        data = {}
        traverse(root)
        return f"{root and root.val}, {data}"

    def deserialize(self, data: str) -> Optional[TreeNode]:
        root_val, data = eval(data)
        if root_val is None:
            return None

        nodes = {root_val: TreeNode(root_val)}
        visit = [root_val]
        while visit:
            val = visit.pop()
            left, right = data[val]
            if left is not None:
                if left not in nodes:
                    nodes[left] = TreeNode(left)
                    visit.append(left)

                nodes[val].left = nodes[left]
            if right is not None:
                if right not in nodes:
                    nodes[right] = TreeNode(right)
                    visit.append(right)

                nodes[val].right = nodes[right]

        return nodes[root_val]
