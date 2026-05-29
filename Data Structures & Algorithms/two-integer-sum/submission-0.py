class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}

        for i,num in enumerate(nums):
            remainder = target - num

            if remainder in record:
                return [record[remainder], i]

            record[num] = i
        
        return [0,0]

