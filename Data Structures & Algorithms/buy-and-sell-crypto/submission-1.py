class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        mxProfit =0 
        for price in prices:
            if price<minprice:
                minprice = price 
            else:
                profit = price - minprice 
                mxProfit = max(profit,mxProfit)

        return mxProfit