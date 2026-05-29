class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1, 2, 4, 6, 
        # 1*(2.4.6), (1)*(4.6), (1.2)*(6), (1.2.4)*1 
        
        # Add 1 to the start and the end
        # we need to record two ways, the product from left to right and right to left

        nums.insert(0,1)
        nums.append(1)

        tempLtr = 1
        tempRtl = 1
        ltr = []
        rtl = []

        l = 0
        r = len(nums) - 1

        while l < len(nums):
            tempLtr *= nums[l]
            tempRtl *= nums[r]

            ltr.append(tempLtr)
            rtl.insert(0, tempRtl)

            l += 1
            r -= 1
        
        nums.pop()
        nums.pop(0)
        
        for i in range(len(nums)):
            nums[i] = ltr[i] * rtl[i+2]

        
        return nums