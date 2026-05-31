class Solution:
    def trap(self, height: List[int]) -> int:
        # We can compute the area by filling the gap of a column that is shorter than minimum of left and right
        l = 0
        r = 0
        temp = []
        filled = height
        area = 0
        index = 0

        while l < len(height) and r < len(height):
        # while index <100:
            index+=1
            
            hl = height[l]
            hr = height[r]

            # print(l,r,hl,hr,temp, area)

            if hl == 0:
                l+=1
                r+=1
                continue

            # Impossible to calculate area
            # if r-l < 2 or hr == 0:
            #     temp.append(r) # store the index, to update later
            #     r+=1
            #     continue

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
        
        # print("=========")
        # print(l,r,hl,hr,temp, area)
        # print(temp)
        # print(height)
        return area




            
        