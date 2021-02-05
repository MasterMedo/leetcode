class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        arr = []
        if root is None:
            return arr

        children = [root]
        while children:
            arr.append(children[-1].val)
            new = []
            for child in children:
                if child.left is not None:
                    new.append(child.left)
                if child.right is not None:
                    new.append(child.right)
            children = new

        return arr
