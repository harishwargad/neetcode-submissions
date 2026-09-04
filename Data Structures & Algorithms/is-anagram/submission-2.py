class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = set(s)
        list_t = set(t)

        if list_s == list_t:
            return True 
        else:
            return False