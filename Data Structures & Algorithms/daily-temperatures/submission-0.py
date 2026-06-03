class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]
        #  1  4  1  2  1  0  0
        # As we iterate we have the information of past days, be it warmer or colder
        # If a warmer day comes, we stop keeping information of the past days
        # We will store a stack of index, and pop them when we found the warmer temperature
        # When we pop it we retrieve the information of the index of the popped / locked days

        stack = []
        result = []
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                colder_temp_index = stack.pop()
                result[colder_temp_index] = i - colder_temp_index
            stack.append(i)
            result.append(0)
        
        return result