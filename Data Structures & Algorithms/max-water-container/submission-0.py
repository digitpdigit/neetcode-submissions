class Solution:
    def calcArea(self, h1: int, h2: int, distance:int) -> int:
        return min(h1, h2) * distance

    def maxArea(self, heights: List[int]) -> int:
        # 1. Bigger the index bigger the area -> for sure
        # 2. Higher the bar bigger the area
        # Two pointers, under those two assumptions, we can make a greedy assumtions
        # That if we have to decrease the index, we gotta make sure the height is bigger
        # so two pointer with index moving towards the bigger height

        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            h1 = heights[l]
            h2 = heights[r]
            distance = r-l
            area = self.calcArea(h1, h2, distance)

            max_area = max(area, max_area)

            if h1 < h2:
                l+=1
            elif h2 < h1:
                r-=1
            else:
                l+=1

        return max_area

        

        
