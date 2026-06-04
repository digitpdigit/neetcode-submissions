class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # i can have two pointer for binary search
        # the r pointer, if the target is smaller or the same (if the same just return), it means the target MUST be on the left side of right pointer
        # the l pointer, if the target is bigger or the same, it means the target must be in the right side of the left pointer


        l, r = 0, len(nums)-1
        while l <= r: 
            m = int((l+r)/2)

            if nums[l] == target:
                return l

            if nums[r] == target:
                return r

            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                if nums[m] > nums[r] and target < nums[l] :
                    l = m+1
                else:
                    r = m-1
            else:
                return m
        
        return -1
            
            
