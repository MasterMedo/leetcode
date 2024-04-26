from bisect import bisect


class MyTree:
    def __init__(self, root: TreeNode):
        self.root = root
        self.depth = 0
        node = root
        while node is not None:
            self.depth += 1
            node = node.left

    def __len__(self):
        return (2**self.depth + 1) // 2

    def __getitem__(self, leaf):
        node = self.root
        for digit in f"{leaf:0b}".zfill(self.depth - 1):
            node = node.left if digit == "0" else node.right
        return (node is None) * 2


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        tree = MyTree(root)
        leafs = bisect(tree, 1)
        return 2 ** (tree.depth - 1) + leafs - 1
