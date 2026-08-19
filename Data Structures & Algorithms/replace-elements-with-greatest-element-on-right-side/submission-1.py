class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        
        for j in range(1, len(arr)):
            max_value = max(arr[j:len(arr)])
            arr[i] = max_value
            i += 1

        arr[-1] = -1
        return arr
