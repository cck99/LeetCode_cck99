class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        min_price = price[0]

        for price in prices[1:]:
            max_price = max(max_price, price - min_price)
            min_price = min(min_price, price)
        return max_price