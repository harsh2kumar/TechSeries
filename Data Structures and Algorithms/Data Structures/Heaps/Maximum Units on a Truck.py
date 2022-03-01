# You are assigned to put some amount of boxes onto one truck. Return the maximum total number of units that can be put on the truck.
# Grokking
# Leetcode https://leetcode.com/problems/maximum-units-on-a-truck/
# Solution https://leetcode.com/problems/maximum-units-on-a-truck/solution/
# Time Complexity The time complexity of O(NlgN)
# Space Complexity The space complexity is O(N).

from typing import List


from heapq import *


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        max_heap = []  # pair(numberOfUnitsPerBox_i, numberOfBoxes_i)
        for n_box, units_box in boxTypes:
            heappush(max_heap, (-units_box, n_box))

        result = 0  # stores max units possible
        while max_heap and truckSize > 0:
            units_box, n_box = heappop(max_heap)
            # if we can put all boxes in our truck
            # add all units -> max_units*n_box
            if truckSize >= n_box:
                result += (-units_box)*n_box
                truckSize -= n_box
            # if we can't put all boxes in our truck
            # add max_possible units -> max_units*truck_size
            else:
                n_box -= truckSize
                result += (-units_box)*truckSize
                truckSize = 0
                heappush(max_heap, (units_box, n_box))
        return result


sol = Solution()
print("[[1,3],[2,2],[3,1]], 4: ", sol.maximumUnits([[1, 3], [2, 2], [3, 1]], 4))
print("[[5,10],[2,5],[4,7],[3,9]], 10: ", sol.maximumUnits(
    [[5, 10], [2, 5], [4, 7], [3, 9]], 10))
