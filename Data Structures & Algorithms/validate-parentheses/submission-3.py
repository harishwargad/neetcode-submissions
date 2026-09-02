class Solution:
    def isValid(self, s: str) -> bool:
        ob = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                ob.append(c)
            elif c == ']' or c == '}' or c == ')':
                if len(ob) != 0:
                    if c == ']' and ob[-1] == '[':
                        ob.pop()
                    elif c == '}' and ob[-1] == '{':
                        ob.pop()
                    elif c == ')' and ob[-1] == '(':
                        ob.pop()
            
        if len(ob) == 0:
            return True 
        else:
            return False
