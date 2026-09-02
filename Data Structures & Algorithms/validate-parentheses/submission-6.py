class Solution:
    def isValid(self, s: str) -> bool:
        ob = []
        matching = {')' : '(', '}' : '{', ']' : '['}

        for c in s:
            if c in matching:
                if (len(ob) == 0) and (ob[-1] != matching[c]):
                    return False
                ob.pop()
            else:
                ob.append(c)

            
        if len(ob) == 0:
            return True 
        else:
            return False
