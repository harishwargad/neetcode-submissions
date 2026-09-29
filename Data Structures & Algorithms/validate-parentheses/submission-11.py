class Solution:
    def isValid(self, s: str) -> bool:
        list_s = list(s)
        dict_s = {')':'(', ']':'[', '}':'{'}

        stack = []

        for i in list_s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')': #or i == '}' or i == ']':
                if stack[-1] == '(':
                    stack.pop()
            elif i == '}':
                if stack[-1] == '{':
                    stack.pop()
            elif i == ']':
                if stack[-1] == '[':
                    stack.pop()

        if stack != None:
            return True 
        else:
            return False