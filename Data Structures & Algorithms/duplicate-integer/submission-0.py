class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # We use set to store already recurring values
        record = set()

        for num in nums:
            if num in record:
                return True
            
            record.add(num)

        return False
        