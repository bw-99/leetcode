class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [float("inf")] * (amount+1)
        min_coins[0] = 0

        for cur_amount in range(1, amount+1):
            for coin in coins:
                if cur_amount - coin >= 0:
                    min_coins[cur_amount] = min(min_coins[cur_amount], min_coins[cur_amount-coin]+1)
        
        return min_coins[-1] if min_coins[-1] != float("inf") else -1
