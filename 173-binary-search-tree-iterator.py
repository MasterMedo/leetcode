def iterator(node: TreeNode) -> int:
    if node is not None:
        yield from iterator(node.left)
        yield node.val
        yield from iterator(node.right)


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.iter = iterator(root)
        self.traverse()

    def traverse(self):
        try:
            self.val = next(self.iter)
        except Exception:
            self.val = None

    def next(self) -> int:
        val = self.val
        self.traverse()
        return val

    def hasNext(self) -> bool:
        return self.val is not None
