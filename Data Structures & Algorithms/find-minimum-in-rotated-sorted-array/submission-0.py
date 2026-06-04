class Solution:
    def findMin(self, nums: List[int]) -> int:
        # so it was originally an ascending order list right
        # when it is rotated theres gonna be a part of the list that sloped
        # We can try to predict which half is rotated
        # rotated means the first element bigger than first element
        # Then we cut in hal to find if its skewed, then half again until it is not skewed

        l, r = 0, len(nums) -1

        if nums[l] < nums[r]:
            return nums[l]

        while l <= r:
            m = int((l + r) /2)

            if m == l:
                l+=1
            # if mid is still bigger than r, we move l, it means the skewed is right side
            elif nums[m] > nums[r]:
                l = m
            # if mid smaller than r we move r, means skewed thing is in the left
            elif nums[m] < nums[r]:
                r = m
            
            if r == l:
                return nums[r]
        
        return nums[r]

        # 3,4,5,6,1,2 [0 5]
        # 5 6 1 2 [2 5]
        # 6 1 2  [3 5]
        # [3 4]
        
