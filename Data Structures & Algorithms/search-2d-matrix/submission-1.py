class Solution:
    def binarySearch(self, nums: List[int], target:int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = int((l+r)/2)

            if nums[m] == target:
                return True
            elif nums[m] > target:
                r = m - 1
            else: 
                l = m + 1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # We do binary search to know which row we should look into
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = int((l+r)/2)

            if matrix[m][0] == target or matrix[m][-1] == target:
                return True
            elif matrix[m][0] > target:
                r = m-1
            elif matrix[m][-1] < target:
                l = m+1
            else:
                return self.binarySearch(matrix[m], target)
            
        
        return False