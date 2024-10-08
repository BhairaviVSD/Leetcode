class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0
        while right < len(prices) :
            print(left, right, prices[right], prices[left])
            if (prices[left] < prices[right]):
                maxProfit = max(maxProfit, prices[right]-prices[left])
                print(prices[right], prices[left])
            else:
                left = right
            right = right + 1
        return maxProfit

        