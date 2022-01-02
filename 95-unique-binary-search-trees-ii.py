from functools import cache


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def generate(left, right):
            if right - left == 0:
                return [TreeNode(right)]
            elif right - left < 0:
                return [None]

            ans = []
            for i in range(left, right + 1):
                lefties = generate(left, i - 1)
                righties = generate(i + 1, right)
                for left_tree in lefties:
                    for right_tree in righties:
                        root = TreeNode(i)
                        root.left = left_tree
                        root.right = right_tree
                        ans.append(root)
            return ans

        return generate(1, n)
