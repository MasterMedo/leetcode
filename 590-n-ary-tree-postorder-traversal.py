class Solution:
    def postorder(self, node: 'Node') -> list[int]:
        if node is None:
            return []

        return [val for child in node.children
                for val in self.postorder(child)] + [node.val]
