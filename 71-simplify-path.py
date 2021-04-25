class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for element in path.split('/'):
            if element:
                if element == '.':
                    pass
                elif element == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(element)

        return '/' + '/'.join(stack)
