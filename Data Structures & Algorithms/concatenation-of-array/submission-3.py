class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        x = 1
        while(x <= 2):
            ans += nums
            x += 1
        return ans

