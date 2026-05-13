# Completed May, 12 2026 | 7.5 minutes

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def parentheses(string, length, o_count, c_count):
            if len(string) == length:
                solutions.append(string)
                return

            if o_count < length / 2:
                parentheses(string + "(", length, o_count + 1, c_count)
            if c_count < o_count:
                parentheses(string + ")", length, o_count, c_count + 1)

        solutions = []
        parentheses("", n * 2, 0, 0)
        return solutions