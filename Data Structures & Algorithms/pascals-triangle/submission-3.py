class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for i in range(numRows):
            # Create a row of length i + 1 filled entirely with 1s
            row = [1] * (i + 1)
            
            # Fill in the inner elements using the previous row
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
                
            res.append(row)
            
        return res