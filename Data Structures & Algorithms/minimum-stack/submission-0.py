class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1] if self.min_stack else val))

    # essentially remove the top
    def pop(self) -> None: 
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    # This forces this class to always know what is the minimum
    def getMin(self) -> int:
        return self.min_stack[-1]
        
