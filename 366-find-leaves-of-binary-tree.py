class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(node: Optional[TreeNode]) -> None:
            nonlocal ans
            if node is None:
                return 0

            i = max(traverse(node.left), traverse(node.right))
            if i >= len(ans):
                ans.append([])

            ans[i].append(node.val)
            return i + 1

        ans = []
        traverse(root)
        return ans
