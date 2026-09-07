class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        for i in range(len(nums)):
            mid = int((l+r) / 2)
            if target == nums[mid]:
                return mid
            else:
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
        return -1
                
