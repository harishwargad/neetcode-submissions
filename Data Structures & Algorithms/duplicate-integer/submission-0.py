class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            for j in nums:
                if i != j:
                    return False
                else: 
                    return True