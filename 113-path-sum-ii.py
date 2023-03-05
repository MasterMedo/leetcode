class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def traverse(node: Optional[TreeNode], targetSum: int, path: List[int]) -> None:
            if node is None:
                return None

            targetSum -= node.val
            path = path + [node.val]
            traverse(node.left, targetSum, path)
            traverse(node.right, targetSum, path)
            if not node.left and not node.right and targetSum == 0:
                arr.append(path)

        arr = []
        traverse(root, targetSum, [])
        return arr
