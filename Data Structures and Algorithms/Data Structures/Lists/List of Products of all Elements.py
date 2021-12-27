# Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number
# stored at that index.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/7DxxOz72RO8
# Leetcode https://leetcode.com/problems/product-of-array-except-self/
# Solution https://leetcode.com/problems/product-of-array-except-self/solution/
# Time Complexity Since this algorithm only traverses over the list twice, it’s in linear time, O(n)O(n).
# Space Complexity The space complexity is O(1).


def find_product(lst):
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product


print(find_product([0, 1, 2, 3]))
