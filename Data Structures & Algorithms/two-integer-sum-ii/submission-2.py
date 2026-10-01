class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(list)

        for i in range(len(numbers)):
            temp = target - numbers[i]
            if temp in mp:
                return [mp[temp], i+1]
            mp[numbers[i]] = i+1
        
        return []