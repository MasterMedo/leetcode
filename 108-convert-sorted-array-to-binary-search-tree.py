class Solution:
    def sortedArrayToBST(self, arr: list[int]) -> TreeNode:
        def make_tree(arr: list[int]) -> TreeNode:
            mid = len(arr) // 2
            node = TreeNode(arr[mid])
            left, right = arr[:mid], arr[mid + 1:]
            if left:
                node.left = make_tree(left)
            if right:
                node.right = make_tree(right)

            return node
        return make_tree(arr) if arr else None
