class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # We can iterate through the whole array
        # Then we keep information somewhere where we can easily decide a bar cant be extended (forgotten)
        # A bar cant be extended if it is bigger than the next bar
        # so something like stack that pop the element if next element is smaller
        # When we pop it we calc the max area

        # 2,1,5,6,2,3
        # 0 2 -> 2
        # 0 1
        # 2 5
        # 3 6
        # 4 2


        stack = [] # will be [[indices, value]]
        max_area = 0

        for i, h in enumerate(heights):
            last_index = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # print(index, height, i-index)
                max_area = max(max_area, height * (i-index))
                last_index = index
            
            stack.append([last_index, h])
            # print(i, stack)

        # Now we got to calculate the rest of remaining unresolved height (on the stack)
        # print(stack)
        for i,h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area
        