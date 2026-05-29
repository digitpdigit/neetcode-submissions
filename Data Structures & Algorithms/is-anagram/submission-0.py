class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If not of same length then not an anagram
        if len(s) != len(t): 
            return False

        str_record = collections.defaultdict(int)

        for i in range(len(s)):
            val_s = s[i]
            val_t = t[i]

            str_record[val_s] += 1
            str_record[val_t] -= 1

            if str_record[val_s] == 0:
                del str_record[val_s]

            if str_record[val_t] == 0:
                del str_record[val_t]
        
        if len(str_record) == 0:
            return True
        
        return False



