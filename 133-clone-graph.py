class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        root = Node(val=node.val)
        seen = {node: root}
        visit = [(root, node)]
        while visit:
            new_node, node = visit.pop()
            for neighbor in node.neighbors:
                if neighbor not in seen:
                    seen[neighbor] = Node(val=neighbor.val)
                    visit.append((seen[neighbor], neighbor))

                new_node.neighbors.append(seen[neighbor])

        return root
