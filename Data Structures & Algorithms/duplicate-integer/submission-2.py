class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_list = sorted(nums)

        for i in range(len(sorted_list)):
            if sorted_list[i] == sorted_list[i - 1]:
                return True 
        return False


