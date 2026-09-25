class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        extra = set()

        for i in nums:
            if i in extra:
                return True
            extra.add(i)
        return False
