# Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number
# stored at that index.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/7DxxOz72RO8
# Leetcode https://leetcode.com/problems/product-of-array-except-self/
# Solution https://leetcode.com/problems/product-of-array-except-self/solution/
# Time Complexity Since this algorithm only traverses over the list twice, it’s in linear time, O(n).
# Space Complexity The space complexity is O(1).


def find_product(lst):
    left = 1
    product = []
    # get product starting from left
    # take product of all left elements
    # at element i, store multiplication of 0..i-1
    # multiply elements to the left of i
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    # multiply elements to the right of i
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product


print(find_product([0, 1, 2, 3]))
