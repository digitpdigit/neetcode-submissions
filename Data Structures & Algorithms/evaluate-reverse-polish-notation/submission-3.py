class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation_set = set(["+", "-", "/", "*"])
        q = collections.deque()

        # We will have LIFO queue, we put token there
        # Until we found the operation
        # then we popleft operation and do the thing
        # Then we put it back on the queue
        # tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        # 10 * (6 / ((9 + 3) * -11)) + 17 + 5
        
        for token in tokens:
            if not token in operation_set:
                q.append(token)
            else:
                second = q.pop()
                first = q.pop()

                # At this point q should be zero
                if token == "+":
                    result = int(first) + int(second)
                if token == "-":
                    result = int(first) - int(second)
                if token == "*":
                    result = int(first) * int(second)
                if token == "/":
                    raw_result = int(first) / int(second)
                    result = int(int(first) / int(second))

                q.append(result)


        return int(q[0])
        