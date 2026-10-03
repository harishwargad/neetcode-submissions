class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        
        # 1. Calculate prefix products (left side)
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
            
        # 2. Multiply by suffix products (right side)
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
            
        return ans