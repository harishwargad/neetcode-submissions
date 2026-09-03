class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cv = set()

        for i in nums:
            if i in cv:
                return True
            else:
                cv.append(i)
        return False
