class Solution:
    def isValid(self, s: str) -> bool:
        ob = []
        matching = {')' : '(', '}' : '{', ']' : '['}

        for c in s:
            if c in matching:
                if ob and ob[-1] == matching[c]:
                    ob.pop()
                else:
                    return False
            else:
                ob.append(c)

            
        if len(ob) == 0:
            return True 
        else:
            return False
