class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        map_close_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c in map_close_open:
                if stack and stack[-1] == map_close_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
     
        return len(stack) == 0
