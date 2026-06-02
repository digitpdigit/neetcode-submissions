class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        # 1 -> 1
        # 1,2 -> 1,2
        # 1,2,1 -> 1,2
        # 2,1,0
       

        # 9,10,9,-7,-4,-8,2,-6
        # 9 -> 9
        # 9,10 -> 10
        # 9,10,9 -> 9,10
        # 9,10,9,-7 -> -7,9,10
        # 9,10,9,-7,-4 -> -4,9,10
        # 10,9,-7,-4,-8 -> -8,-4,9,10
        # 9,-7,-4,-8,2 -> 2,-4,9
        
        

        result = []

        # When old number goes, we dequeue only if the index matches the biggest
        # If new number comes, if its bigger than biggest we just forget everything
        # If new number comes, if its same as the biggest -> update index
        # If new number comes, if its bigger than the smallest -> While the new number is bigger than the back candidate, keep removing candidates.
        # If new number comes and it is the same as smallest -> update index
        # If new number comes and it is smaller then smallest -> appendLeft

        # Order
        # is valid? if it is then we move l
        # move r

        # will hold values and index
        queue = collections.deque()
        l = 0
        r = 0
        is_valid_window = False

        while r < len(nums):
            if r == 0:
                queue.append({
                    "value": nums[r],
                    "index": r
                })
                r+=1
                continue

            # Is valid? if it does we move l first
            if (r-l) == k:
                old_number = nums[l]
                # print(old_number, queue)

                biggest = queue[-1]
                if old_number == biggest["value"] and l == biggest["index"]:
                    queue.pop()

                l+=1
            
            # Process new number
            new_number = nums[r]
            if new_number >= queue[-1]["value"]:
                queue = deque([{
                    "value": new_number,
                    "index": r
                }])        
            elif new_number == queue[0]["value"]:
                queue[0] = {
                    "value": new_number,
                    "index": r
                }
            elif new_number > queue[0]["value"]:
                while queue[0]["value"] < new_number:
                    queue.popleft()
                queue.appendleft({
                    "value": new_number,
                    "index": r
                })
                
            elif new_number < queue[0]["value"]:
                queue.appendleft({
                    "value": new_number,
                    "index": r
                })

            # Valid window after moving l if it does
            if (r-l + 1) == k:
                result.append(queue[-1]["value"])

           
            r+=1

          


        return result 

        