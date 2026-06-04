class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max k should be the highest pile there is right
        # min k should be the sum of all pile / max hours

        max_k = 0

        for pile in piles:
            max_k = max(max_k, pile)
        
        # We got max_k, so we can search between 1 to max_k, which smallest number that can satisfy sum_piles/m == h
        l,r = 1, max_k
        smallest_k = float('inf')
        while l <= r:
            m = int((l+r)/2)

            hours = 0
            for i in piles:
                hours += math.ceil(i/m)

            if hours > h:
                l = m + 1
            else:
                r = m - 1
                smallest_k = min(m, smallest_k)

        return smallest_k
        