class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        # Valid window = (length - most char occurences) <= k
        # Iterate with sliding window, and move our pointers towards the end
        # 1. If valid then right pointer += 1
        # 2. If invalid then left pointer += 1
        # XYYX, k=2
        # XY v
        # XYY v
        # XYYX v
        # AAABABB, k=1
        # AAABAB
        # AABAB
        # ABAB
        # BABB

        l = 0
        r = 1
        result = 0
        record = collections.defaultdict(int)

        record[s[l]] += 1
        record[s[r]] += 1

        most_frequent = s[l]

        while r < len(s):
            cl = s[l]
            cr = s[r]
            temp_length = r - l + 1
            is_valid = (temp_length - record[most_frequent]) <= k

            if is_valid:
                result = max(result, temp_length)
                r += 1

                if r >= len(s):
                    break

                record[s[r]] += 1

                if record[s[r]] > record[most_frequent]:
                    most_frequent = s[r]
            else:
                record[cl] -= 1

                if cl == most_frequent:
                    # Look for the next most_frequent
                    for char, occurences in record.items():
                        if record[char] > record[most_frequent]:
                            most_frequent = char
                
                l+=1
        
        return result



            





        

