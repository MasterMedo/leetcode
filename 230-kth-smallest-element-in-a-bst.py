class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def helper(node: TreeNode, smaller=0):
            if node is None:
                return False, 0, 0

            found, smaller_left, val = helper(node.left, smaller)
            if found:
                return True, 0, val

            if smaller + smaller_left == k - 1:
                return True, 0, node.val

            found, smaller_right, val = helper(node.right, smaller + smaller_left + 1)
            if found:
                return True, 0, val

            return False, smaller_left + smaller_right + 1, 0

        return helper(root)[2]
