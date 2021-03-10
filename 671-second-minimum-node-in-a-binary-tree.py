from heapq import heappushpop
from math import inf


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def traverse(node: TreeNode) -> None:
            if node is not None:
                if node.val not in seen:
                    seen.add(node.val)
                    heappushpop(heap, -node.val)

                traverse(node.left)
                traverse(node.right)

        seen = set()
        heap = [-inf, -inf]
        traverse(root)
        return -heap[0] if heap[0] != -inf else -1
