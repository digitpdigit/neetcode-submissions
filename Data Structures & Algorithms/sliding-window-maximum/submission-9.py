class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums


        result = []

        # 1 2 1 0 4 2 6
        # 1 -> [1]
        # 1 2 -> [2]
        # 1 2 1 -> [2, 1] -> 1 has a chance to become the biggest
        # 2 1 0 -> [2, 1, 0] -> 0 has a chance too
        # 1 0 4 -> [4]

        # When a number comes and it is bigger than the biggest we remove all that is smaller
        # When it is smaller or the same we put it in the rightside (append)
        # When a number goes we remove from the queue, since it is an older one we should be able to popleft
        # So the dequeue should be in index instead (?) 
        # why, to ensure we dont pop the wrong index for example 8 0 8 1 k = 3 -> [8,8] -> [8]

        l = 0
        r = 0
        q = collections.deque()

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Check if we need to popleft, if the biggest is old (less than left)
            if l > q[0]:
                q.popleft()

            # If its a valid window
            if r + 1 >= k:
                result.append(nums[q[0]])
                l+=1
            
            r+=1
        return result 

        