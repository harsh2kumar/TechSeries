# Analyze User Website Visit Pattern
# Grokking
# Leetcode https://leetcode.com/problems/analyze-user-website-visit-pattern/
# Solution https://leetcode.com/problems/analyze-user-website-visit-pattern/solution/
# Time Complexity O(n*n!).
# Space Complexity O(n*n!).

from typing import List
import heapq
from collections import defaultdict
from itertools import combinations


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        # zip the time, user and website to one list
        tuw = list(zip(timestamp, username, website))

        # we need to sort them by time --> username --> website
        sorted_tuw = sorted(tuw)

        # We will polulate a user history hashmap of various pages visited. The hashmap is of type {user: [pages]}
        user_history = defaultdict(list)
        for t, u, w in sorted_tuw:
            user_history[u].append(w)

        # get various combinations possible for various users
        pattern_count = defaultdict(int)
        for user, websites in user_history.items():
            # get various combinations possible for various users in the pair of 3 and add them to set so that they are unique
            user_combinations = set(combinations(websites, 3))
            # for every pair of userCombination, we will update the count. This count will make sense for second user onwards having the same pattern
            for uc in user_combinations:
                pattern_count[uc] += 1

        # We need to sort both the keys(pattern lexographically) from from min to max and values(score) form max to min
        # If we inverse the values of keys from val to -val, then we can sort both of them in ascending order, using minheap
        # here invertedValues represent the values with -ve sign added to it
        max_heap_vals = [-i for i in pattern_count.values()]

        # Zip both the keys and values so that we can sort them. We are placing invertedValues first as we first need to sort by score and then need to sort lexographically in natural order
        max_heap_freq_websites = list(zip(max_heap_vals, pattern_count.keys()))

        # Heapify will sort them in the ascending order as this is min heapify operation and will take nlog(n) time as both siftup and siftdown operations are called
        heapq.heapify(max_heap_freq_websites)

        # Top of the heap will represent the sorted value by -ve score
        return max_heap_freq_websites[0][1]


sol = Solution()
print('["joe","joe","joe","james","james","james","james","mary","mary","mary"], [1,2,3,4,5,6,7,8,9,10], ["home","about","career","home","cart","maps","home","home","about","career"]: ', sol.mostVisitedPattern(
    ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]))
print('["ua","ua","ua","ub","ub","ub"], [1,2,3,4,5,6], ["a","b","a","a","b","c"]: ', sol.mostVisitedPattern(
    ["ua", "ua", "ua", "ub", "ub", "ub"], [1, 2, 3, 4, 5, 6], ["a", "b", "a", "a", "b", "c"]))
