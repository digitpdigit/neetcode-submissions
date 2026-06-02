class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = collections.deque()
        for char in s:
            if char == "[" or char =="{" or char == "(":
                stack.append(char)
            elif stack:
                last = stack.pop()
                if last == "{" and char == "}":
                    continue
                elif last == "[" and char == "]":
                    continue
                elif last == "(" and char == ")":
                    continue
                return False
            else: 
                return False
        
        return len(stack) == 0
