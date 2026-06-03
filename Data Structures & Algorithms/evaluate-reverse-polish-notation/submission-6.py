class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation_set = set(["+", "-", "/", "*"])
        stack = []

        # We will have LIFO queue, we put token there
        # Until we found the operation
        # then we popleft operation and do the thing
        # Then we put it back on the queue
        # tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        # 10 * (6 / ((9 + 3) * -11)) + 17 + 5
        
        for token in tokens:
            if not token in operation_set:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()

                # At this point q should be zero
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                else: # token == "/"
                    stack.append(int(first / second))

        return stack[0]
        