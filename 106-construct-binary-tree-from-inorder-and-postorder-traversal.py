class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        node = TreeNode(postorder[-1])
        # could use binary search but meh
        i = 0
        while inorder[i] != postorder[-1]:
            i += 1
        node.left = self.buildTree(inorder[:i], postorder[:i])
        node.right = self.buildTree(inorder[i + 1:], postorder[i:len(postorder) - 1])
        return node
