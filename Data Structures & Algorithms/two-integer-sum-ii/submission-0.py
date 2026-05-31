class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        record = {}

        for index, number in enumerate(numbers):
            missing = target - number
            if missing in record:
                return [record[missing] + 1, index+1]
            
            record[number] = index
            
        return []