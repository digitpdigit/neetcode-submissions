class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Dict to save consecutive count
        cons_record = collections.defaultdict(bool)

        for num in nums:
            cons_record[num] = True

        starting_sequence = []
        for num in nums:
            prev = num - 1

            if prev in cons_record:
                continue
            else:
                starting_sequence.append(num)
        
        n_length = len(nums)
        longest = 0
        
        for seq in starting_sequence:
            temp_length = 0
            while seq in cons_record:
                temp_length += 1
                seq += 1
            
            longest = max(temp_length, longest)
        
        return longest
            

        

            
