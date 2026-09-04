class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = sorted(list(s))
        list_t = sorted(list(t))

        if list_s == list_t:
            return True 
        else:
            return False