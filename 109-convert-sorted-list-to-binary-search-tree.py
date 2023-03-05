class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def makeTree(arr: List[int]) -> Optional[TreeNode]:
            if not arr:
                return None

            i = len(arr) // 2
            node = TreeNode(arr[i])
            node.left = makeTree(arr[:i])
            node.right = makeTree(arr[i + 1:])
            return node

        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next

        return makeTree(arr)
