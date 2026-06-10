class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Naive solution would to store the set of val 
        # If we find a match we return the val

        # Lets do the naive first
        record = set()
        for n in nums:
            if n in record:
                return n
            else:
                record.add(n) 