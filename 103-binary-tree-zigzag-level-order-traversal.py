class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []
        output = []
        level = [root]
        reverse = False
        while level:
            output.append([])
            next_level = []
            order = range(len(level)) if not reverse else range(len(level) - 1, -1, -1)
            for i in order:
                node = level[i]
                output[-1].append(node.val)
                children = [node.left, node.right] if not reverse else [node.right, node.left]
                for child in children:
                    if child is not None:
                        next_level.append(child)
            level = next_level if not reverse else next_level[::-1]
            reverse = not reverse
        return output
