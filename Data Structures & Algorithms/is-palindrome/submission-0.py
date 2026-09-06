class Solution:
    def isPalindrome(self, s: str) -> bool:
        from_forward = list(s)
        from_backward = reversed(list(s))

        print(from_forward)
        print(from_backward)

        # if from_forward == from_backward:
        #     return True 
        # else:
        #     return False 