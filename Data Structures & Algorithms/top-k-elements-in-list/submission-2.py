class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences_to_values_map = collections.defaultdict(list)
        values_to_occurences_map = collections.defaultdict(int)
        occurences_set = set()

        for num in nums:
            values_to_occurences_map[num]+=1

        for value in values_to_occurences_map:
            occurences = values_to_occurences_map[value]
            occurences_set.add(occurences)
            occurences_to_values_map[occurences].append(value)
        
        result = []

        for i in range(len(nums), 0, -1):
            result += occurences_to_values_map[i]

        return result[0:k]
        


