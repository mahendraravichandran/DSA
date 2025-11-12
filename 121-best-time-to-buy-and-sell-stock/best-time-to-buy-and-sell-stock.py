class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        l,r = 0,1
        while r < len(prices):
            sums = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r 
            elif sums > total:
                total = sums
            r+=1
        return total
             