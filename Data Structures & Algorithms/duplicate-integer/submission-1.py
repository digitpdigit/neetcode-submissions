class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # For easy checking, we can use dictionary
        record = {}

        for n in nums:
            if n in record:
                return True
            else:
                record[n] = True

        return False
        