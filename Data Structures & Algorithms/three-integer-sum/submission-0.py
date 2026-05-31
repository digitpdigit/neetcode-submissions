class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                result.append([nums[l], nums[r]])
                l+=1
            elif nums[l] + nums[r] > target:
                r-=1
            else:
                l+=1

        return result
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #  0 1 2 3 4
        #  1 1 1 
        nums = sorted(nums)
        record = set()
        result = []
        for index, num in enumerate(nums):
            if index + 2 == len(nums):
                break
            
            target = 0 - num

            # we do two sum on the rest of the array
            rest = nums[(index+1):]
            two_sum_results = self.twoSum(rest, target)
            if len(two_sum_results):
                for res in two_sum_results:
                    temp = [num] + res
                    key = "".join([f"{i}" for i in temp])
                    if key in record:
                        continue
                    
                    result.append(temp)
                    record.add(key)

        
        return result
            
        