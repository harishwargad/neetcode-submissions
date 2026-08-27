class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        closeToOpen = {')' : '(', '}' : '{', ']' : '['}
        
        for c in s:
            if c in closeToOpen:
                if a and a[-1] == closeToOpen[c]:
                    a.pop()
                else:
                    return False 
            else:
                a.append(c)
        
        return True if not a else False 