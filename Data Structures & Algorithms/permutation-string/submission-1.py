class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1. Permutation meaning the substring on s2 contains exact amount of char occurences of s1

        if len(s1) > len(s2): 
            return False
        
        if len(s1) == 0:
            return True

        s1_record = collections.defaultdict(int)
        for char in s1:
            s1_record[char] += 1

        s1_length = len(s1)

        temp_record = collections.defaultdict(int)
        for char in s2[0:s1_length]:
            temp_record[char] += 1

        if temp_record == s1_record:
            return True
            
        # Move a window of s1_length, move it one by one until the end or until we found the permutation
        l = 0
        r = s1_length - 1

        while r < len(s2):
            temp_record[s2[l]] -= 1
            if temp_record[s2[l]] <= 0:
                del temp_record[s2[l]]

            l += 1
            r += 1
            if r >= len(s2):
                break
            temp_record[s2[r]] += 1

            if temp_record == s1_record:
                return True

        return False



