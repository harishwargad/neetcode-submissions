class Solution:
    def isValid(self, s: str) -> bool:
        list_s = list(s)
        dict_s = {')':'(', ']':'[', '}':'{'}

        stack = []

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')': #or i == '}' or i == ']':
                if stack[-1] == '(':
                    stack.pop()
                return False
            elif i == '}':
                if stack[-1] == '{':
                    stack.pop()
                return False
            elif i == ']':
                if stack[-1] == '[':
                    stack.pop()
                return False

        if stack != None:
            return True 
        else:
            return False