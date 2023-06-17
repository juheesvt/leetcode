class Solution:
    def isValid(self, s: str) -> bool:

        stack = list()
        for parentheses in s:
            if parentheses == ')':
                if len(stack) and '(' == stack[-1]:
                    del stack[-1]
                else:
                    return False
            elif parentheses == ']':
                if len(stack) and '[' == stack[-1]:
                    del stack[-1]
                else:
                    return False

            elif parentheses == '}':
                if len(stack) and '{' == stack[-1]:
                    del stack[-1]
                else:
                    return False
            else:
                stack.append(parentheses)

        return True if len(stack) == 0 else False
