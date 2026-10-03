class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            mul = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    mul *= nums[j]
            ans.append(mul)

        return ans