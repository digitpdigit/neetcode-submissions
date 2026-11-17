class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We can record the occurences of each number in nums
        # Then we map the occurence to the array of number

        num_to_occurence = collections.defaultdict(int)
        
        for num in nums:
            num_to_occurence[num] += 1

        occurence_to_nums = collections.defaultdict(list)
        for num, occurence in num_to_occurence.items():
            occurence_to_nums[occurence].append(num)

        # We look for the max occurence first, countdown to 0
        result = []
        for i in range(len(nums), 0, -1):
            if i in occurence_to_nums:
                result += occurence_to_nums[i]
            
            if len(result) >= k:
                break
            
        
        return result[0:k]

            
  


