class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        solutions = []

        def p(cOpen, cClose, pString):
            # means we're done with this string here
            if cClose == n:
                solutions.append(pString)
            if cClose < cOpen:
                p(cOpen, cClose+1, pString+')')
            if cOpen < n:
                p(cOpen+1, cClose, pString+'(')
        p(1, 0, '(')
        return solutions

s = Solution()
print(s.generateParenthesis(3))