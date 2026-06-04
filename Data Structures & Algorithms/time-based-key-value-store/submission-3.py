class TimeMap:

    def __init__(self):
        self.record = collections.defaultdict(list) # Map of key to list of value, timestamp
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.record[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        records = self.record[key]

        if len(records) == 0:
            return ""

        # We do binary search to find the exact value, if we cant find it then we return the last pointer
        l, r = 0, len(records) - 1

        # Check if we're getting with timestamp that is smaller than even the smallest
        if records[0][0] > timestamp:
            return ""

        while l<=r:
            m = (l+r) // 2
            # print(l,r,m, records, timestamp)


            if records[m][0] == timestamp:
                return records[m][1]

            if timestamp > records[m][0]:
                l = m + 1
            else:
                r = m - 1
       
        return records[r][1]
