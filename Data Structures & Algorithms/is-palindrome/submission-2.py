class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_chars = [char.lower() for char in s if char.isalnum()]
    
        return cleaned_chars == cleaned_chars[::-1]