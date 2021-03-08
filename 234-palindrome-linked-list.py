class Solution:
    def isPalindrome(self, node: ListNode) -> bool:
        arr = []
        while node:
            arr.append(node.val)
            node = node.next

        return arr == arr[::-1]
