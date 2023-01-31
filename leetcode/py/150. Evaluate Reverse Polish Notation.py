class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for x in tokens:
            if x in operators:
                # get top two numbers from stack and apply it on them
                one = stack.pop()
                two = stack.pop()
                if x == '+':
                    new = one+two
                elif x == '-':
                    new = two+one
                elif x == '*':
                    new = two*one
                elif x == '/':
                    new = int(two/one)
                stack.append(new)
            else:
                stack.append(int(x))
            print(stack)
        return stack[-1]                
        
s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))