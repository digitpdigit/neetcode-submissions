class Solution:
    def trap(self, height: List[int]) -> int:
        # We can compute the area by filling the gap of a column that is shorter than minimum of left and right
        l = 0
        r = 0
        temp = []
        area = 0

        while l < len(height) and r < len(height):
            
            hl = height[l]
            hr = height[r]


            if hl == 0:
                l+=1
                r+=1
                continue

            # Calculate the area
            min_h = min(hr, hl)
            for t in temp:
                ht = height[t]

                if min_h > ht:
                    diff = min_h - ht
                    area += diff
                    height[t] = min_h            

            if hr >= hl and r-l >= 1:
                l = r
                temp = []    
            else:
                temp.append(r) # store the index, to update later
                r+=1    
        
        return area




            
        