class Solution:
    def calPoints(self, operations: List[str]) -> int:
        signs = ['+', 'C', 'D']
        op_copy = []
        
        for i in operations:
            if i == '+':
                op_copy.append(op_copy[-1] + op_copy[-2])
            elif i == 'D':
                op_copy.append(op_copy[-1] * 2)
            elif i == 'C':
                op_copy.pop()
            else:
                op_copy.append(int(i))
        
        return sum(op_copy)