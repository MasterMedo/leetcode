class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def traverse(node: Optional[TreeNode], child=""):
            nonlocal ups, downs
            if node is None:
                return [False, False]

            a1, b1 = traverse(node.left, "L")
            a2, b2 = traverse(node.right, "R")
            values = [a1 or a2, b1 or b2]
            if values[0] and values[1]:
                return values

            if node.val == startValue:
                if values[1]:
                    return [True, True]
                values[0] = True

            if node.val == destValue:
                if values[0]:
                    return [True, True]
                values[1] = True

            if values[0]:
                ups.append("U")

            if values[1]:
                downs.append(child)

            return values

        ups = []
        downs = []
        traverse(root)
        return "".join(ups + downs[::-1])
