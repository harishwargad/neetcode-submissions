class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        extra = []

        for i in range(len(nums)):
            if nums[i] not in extra:
                extra.append(nums[i])
            elif nums[i] in extra:
                return True
        return False
