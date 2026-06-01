class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        if len(t) > len(s):
            return ""

        # 1. Valid permutation meaning each char in t exists in the substring
        # 2. Substring length should be minimum of t length

        diff = 0
        t_record = collections.defaultdict(int)
        for char in t:
            t_record[char] += 1
            diff += 1

        temp_record = collections.defaultdict(int)

        l = 0
        if s[l] in t_record:
            t_record[s[l]] -= 1
            diff -= 1 
        
        r = 0

        while r <= len(s):
            # print(l,r, diff)
            
            if diff > 0:
                r += 1

                if r >= len(s):
                    break
                
                if s[r] in t_record:
                    t_record[s[r]] -= 1
                    if t_record[s[r]] >= 0:
                        diff -= 1
            else:
                temp_result = "".join(s[l:r+1])
                if result == "":
                    result = temp_result
                else:
                    result = temp_result if len(temp_result) < len(result) else result

                if s[l] in t_record:
                    t_record[s[l]] += 1
                    if t_record[s[l]] > 0:
                        diff += 1

                if l >= len(s) - 1:
                    break

                l += 1
        
        return result

        # c a b w e f g e w c w  a  e  f  g  c  f
        # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16



