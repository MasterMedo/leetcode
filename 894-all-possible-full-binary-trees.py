from functools import cache


class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        if n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode()]

        trees = []
        for i in range(n):
            j = n - 1 - i
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(j):
                    root = TreeNode()
                    root.left = left
                    root.right = right
                    trees.append(root)

        return trees
