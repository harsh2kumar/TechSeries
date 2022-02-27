# You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.
# # Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
# Grokking
# Leetcode https://leetcode.com/problems/the-kth-factor-of-n/
# Solution https://leetcode.com/problems/the-kth-factor-of-n/
# Time Complexity O(sqrt(n)).
# Space Complexity O(min(k, sqrt(N​)) to store the list of divisors.

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        divisors, sqrt_n = [], int(n**.5)
        for i in range(1, sqrt_n+1):
            if n % i == 0:
                k -= 1
                divisors.append(i)
                if k == 0:
                    return i
        # if n is a perfect square
        # we need ot skip the duplicate
        if (sqrt_n**2 == n):
            k += 1

        len_div = len(divisors)
        return n//divisors[len_div-k] if k <= len_div else -1


sol = Solution()
print("12, 3: ", sol.kthFactor(12, 3))
print("7, 2: ", sol.kthFactor(7, 2))
print("4, 4: ", sol.kthFactor(4, 4))
