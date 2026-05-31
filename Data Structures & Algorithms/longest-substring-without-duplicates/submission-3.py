class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        record = set()

        l = 0
        r = 1

        record.add(s[l])

        longest = 1
        temp = 1

        while r < len(s):
            sl = s[l]
            sr = s[r]

            if sr in record:
                if sr == sl:
                    temp -= 1
                    l += 1
                else:
                    temp = 0
                    l = r
                    record = set()

            record.add(sr)
            temp += 1

            r+=1

            longest = max(longest, temp)

        return longest

            

