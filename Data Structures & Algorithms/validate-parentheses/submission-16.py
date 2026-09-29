class Solution:
    def isValid(self, s: str) -> bool:
        list_s = list(s)
        dict_s = {')':'(', ']':'[', '}':'{'}

        stack = []

        for i in list_s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif stack != None:
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
            else:
                return False

        if stack != None:
            return True 
        else:
            return False