class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        
        max_amount = 0

        while r < len(prices):
            r_price = prices[r]
            l_price = prices[l]

            # if r_price bigger, we make transaction
            if r_price > l_price:
                max_amount = max(r_price - l_price, max_amount)
            else:
                l = r


            r+=1

        return max_amount
            
            

