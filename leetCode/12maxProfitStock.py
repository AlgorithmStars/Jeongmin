class Solution:
    def maxProfit(self, prices:list[int]) -> int:
        currentMin, maxprofit = float('inf'), 0
        for p in prices:
            currentMin = min(p, currentMin)
            if p - currentMin > maxprofit:
                maxprofit = p - currentMin

        return maxprofit
            
sol = Solution()
print(sol.maxProfit([7,6,4,3,1]))
print(sol.maxProfit([7,1,5,3,6,4]))
