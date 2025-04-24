class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+" or token == "-" or token == "/" or token == "*":
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                result = 0
                if token == "+":
                    result = op2 + op1
                if token == "-":
                    result = op2 - op1
                if token == "/":
                    result = int(op2 / op1)
                if token == "*":
                    result = op2 * op1
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]