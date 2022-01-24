class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        mark = "mark"
        while True:
            if p is not None:
                if getattr(p, mark, None) is not None:
                    return p

                setattr(p, mark, mark)
                p = p.parent

            if q is not None:
                if getattr(q, mark, None) is not None:
                    return q

                setattr(q, mark, mark)
                q = q.parent
