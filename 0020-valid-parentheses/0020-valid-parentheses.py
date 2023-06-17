class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = list()
        parentheses_dict = {'}': '{', ']': '[', ')': '('}
        
        for parentheses in s:
            if parentheses in parentheses_dict.keys():
                if stack and stack[-1] == parentheses_dict[parentheses]:
                    del stack[-1]
                else:
                    return False
            else:
                stack.append(parentheses)
        print(stack)
        return True if len(stack) == 0 else False
