class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return
        arr = [root]
        while arr:
            new_arr = []
            for i in range(len(arr)):
                if arr[i].left is not None:
                    new_arr.append(arr[i].left)

                if arr[i].right is not None:
                    new_arr.append(arr[i].right)

                if len(arr) > i + 1:
                    arr[i].next = arr[i + 1]

            arr = new_arr

        return root
