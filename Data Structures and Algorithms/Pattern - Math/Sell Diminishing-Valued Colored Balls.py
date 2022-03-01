# You have an inventory of different colored balls, and there is a customer that wants orders balls of any color. Return the maximum total value that you can
# attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.
# Grokking
# Leetcode https://leetcode.com/problems/sell-diminishing-valued-colored-balls/
# Solution https://leetcode.com/problems/sell-diminishing-valued-colored-balls/solution/
# Time Complexity O(N*logN), as we'll go thorough the list of all balls at most once and we sort the inventory array in descending order.
# Space Complexity O(1)

from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def getSum(start, end):
            return (start*(start+1))//2 - (end*(end+1))//2

        # sort in reverse order since we want to maximize sale
        inventory.sort(reverse=True)
        factor = 1  # how many colors have the same amount of inventory remaining
        n = len(inventory)
        i = 0
        ans = 0

        while orders > 0:
            # if we can make sale for all factor
            # we check i<n-1, because we are using i+1
            if i < n-1 and inventory[i] > inventory[i+1] and orders >= factor*(inventory[i]-inventory[i+1]):
                ans += factor*getSum(inventory[i], inventory[i+1])
                orders -= factor*(inventory[i]-inventory[i+1])
            # if we cannot make sale for all factors
            elif i == n-1 or inventory[i] > inventory[i+1]:
                sell_all_times = orders // factor
                ans += factor*getSum(inventory[i], inventory[i]-sell_all_times)
                remaining_orders = orders % factor
                ans += remaining_orders * (inventory[i]-sell_all_times)
                break

            # if inventory[i] == inventory[i+1]:
            i += 1
            factor += 1

        mod = 10**9+7
        return ans % mod


sol = Solution()
print("[2,5], 4: ", sol.maxProfit([2, 5], 4))
print("[3,5], 6: ", sol.maxProfit([3, 5], 6))
print("[1000,1000], 2: ", sol.maxProfit([1000, 1000], 2))
