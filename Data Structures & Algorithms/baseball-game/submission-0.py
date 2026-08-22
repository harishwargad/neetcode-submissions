class Solution:
    def calPoints(self, operations: List[str]) -> int:
        signs = ['+', 'C', 'D']
        op_copy = []
        
        for i in operations:
            if i == '+':
                addition = op_copy[-1] + op_copy[-2]
                op_copy.append(addition)
            elif i == 'D':
                mult = op_copy[-1] * 2
                op_copy.append(mult)
            elif i == 'C':
                op_copy.pop()
            else:
                op_copy.append(int(i))
        
        return sum(op_copy)