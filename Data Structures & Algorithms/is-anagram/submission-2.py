class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        # So basically we can record what letters construct the word and how many times it appear
        # Then we compare it

        record = {c: 0 for c in s}
        for char in s:
            record[char] += 1

        # Check on the second thing
        for char in t:
            if char not in record:
                return False
            elif record[char] == 0:
                return False
            else:
                record[char] -= 1

        
        return True
  

