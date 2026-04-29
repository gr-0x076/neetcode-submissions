class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mP = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price

            elif price - min_price > mP:
                mP = price - min_price

        return mP