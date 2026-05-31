class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while True:
            temp_sum = numbers[l] + numbers[r]

            if temp_sum == target:
                return [l+1, r+1]
            elif temp_sum > target:
                r-=1
            else: 
                l+=1