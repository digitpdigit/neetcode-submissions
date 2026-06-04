class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # i can have two pointer for binary search

        # If target smaller than x then it must be on the left side of x
        # If target bigger than x then it must be on the right side of x
        
        l,r = 0, len(nums) - 1

        while l<=r:
            m = (l+r) //2

            if nums[m] == target:
                return m
            
            # Lets see, which part is breakpoint
            if nums[m] >= nums[l]:
                # We got break point on the right
                # Meaning left side is ascending normally, meaning we should move l
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # We got break point on the left
                # Meaning the right side is ascending normally
                if target > nums[m] and target < nums[l]:
                    l = m+1
                else:
                    r = m-1

              
                
        return -1



            
