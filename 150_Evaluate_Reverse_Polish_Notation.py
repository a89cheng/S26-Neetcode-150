# Completed May, 11 2026 | 35 minutes

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = {'+',"-","*","/"}
        calculation_set = []

        for value in tokens:
            if value not in signs:
                calculation_set.append(int(value))
            else:
                value2 = calculation_set.pop(-1)
                value1 = calculation_set.pop(-1)
                if value == "+":
                    calculation_set.append(value1+value2)
                elif value == "-":
                    calculation_set.append(value1-value2)
                elif value == "*":
                    calculation_set.append(value1*value2)
                else:
                    #Always truncates towards 0
                    calculation_set.append(int(value1/value2))

        return calculation_set[0]