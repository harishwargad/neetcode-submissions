class Solution:
    def isPalindrome(self, s: str) -> bool:
        # updated_s = ["".join(s.split()).isalnum()]
        cleaned_chars = [char.lower() for char in s if char.isalnum()]
        # us = updated_s.lower()

        # from_forward = list(updated_s)
        # from_backward = list(reversed(list(updated_s)))

        # if from_forward == from_backward:
        #     return True 
        # else:
        #     return False 
        return cleaned_chars == cleaned_chars[::-1]