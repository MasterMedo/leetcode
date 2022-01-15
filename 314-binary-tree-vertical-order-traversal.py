from collections import defaultdict, deque


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        columns = defaultdict(list)
        min_col = max_col = 0
        visit = deque([(root, 0)])
        while visit:
            node, col = visit.popleft()
            columns[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            if node.left is not None:
                visit.append((node.left, col - 1))
            if node.right is not None:
                visit.append((node.right, col + 1))

        return [columns[col] for col in range(min_col, max_col + 1)]
