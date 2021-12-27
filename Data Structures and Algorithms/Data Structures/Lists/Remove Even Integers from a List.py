# Implement a function that removes all the even elements from a given list. Name it `remove_even(lst)`.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/N8MJQNYyJPL
# Leetcode
# Solution
# Time Complexity Since the entire list has to be iterated over, this solution is in O(n) time.
# Space Complexity Since in the worst case entire list can be odd, the space complexity is O(n).


def remove_even(lst):
    # using list comprehension
    return [num for num in lst if num%2!=0]

    odds = []  # Create a new empty list
    for number in lst:  # Iterate over input list
        # Check if the item in the list is NOT even
        # ('%' is the modulus symbol!)
        if number % 2 != 0:
            odds.append(number)  # If it isn't even append it to the empty list
    return odds  # Return the new list


print(remove_even([3, 2, 41, 3, 34]))
