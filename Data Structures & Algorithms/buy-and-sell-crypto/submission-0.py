class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMax = 0
        l, r = 0, 1
        while(r < len(prices)):
            # move two pointers until the left is smaller than the right value
            if(prices[l] > prices[r]):
                l = r
                r += 1

            else: # possible new max profit
                curMax = max(curMax, max(0, prices[r] - prices[l]))
                r += 1
        return curMax