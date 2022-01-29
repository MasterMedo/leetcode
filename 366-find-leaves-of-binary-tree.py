class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(node: TreeNode, parent: Optional[TreeNode] = None, left: bool = False) -> None:
            nonlocal leaves
            if node.left is None and node.right is None:
                leaves.append(node)
            else:
                if node.left is not None:
                    traverse(node.left, node, left=True)
                if node.right is not None:
                    traverse(node.right, node, left=False)

            node.parent = (parent, left)

        leaves = []
        traverse(root)
        ans = []
        while leaves:
            new_leaves = []
            ans.append([])
            for leaf in leaves:
                ans[-1].append(leaf.val)
                parent, left = leaf.parent
                if parent is None:
                    continue

                if left:
                    parent.left = None
                else:
                    parent.right = None

                if parent.left is None and parent.right is None:
                    new_leaves.append(parent)

            leaves = new_leaves

        return ans
