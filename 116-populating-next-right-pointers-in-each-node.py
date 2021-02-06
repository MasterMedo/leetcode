class Solution:
    def connect(self, root):
        node = root
        while node and node.left:
            left = node.left
            while node:
                node.left.next = node.right
                node.right.next = node.next and node.next.left
                node = node.next
            node = left
        return root
