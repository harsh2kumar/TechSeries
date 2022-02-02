# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# Grokking
# Leetcode https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Solution https://leetcode.com/problems/letter-combinations-of-a-phone-number/solution/
# Time Complexity O(N.4^N) where N is the length of digits. Note that 4 in this expression is referring to the maximum value length in the hash map,
# and not to the length of the input.
# Space Complexity O(N), where N is the length of digits.


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0:
            return []
        combinations = []
        # Map all the digits to their corresponding letters
        letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(index, current):
            # If the path is the same length as digits, we have a complete combination
            if len(current) == len(digits):
                combinations.append("".join(current))
                return  # Backtrack

            # Get the letters that the current digit maps to, and loop through them
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                current.append(letter)
                # Move on to the next digit
                backtrack(index+1, current)
                # Backtrack by removing the letter before moving onto the next
                current.pop()
        # Initiate backtracking with an empty path and starting index of 0
        backtrack(0, [])
        return combinations


if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("23"))
    print(sol.letterCombinations(""))
    print(sol.letterCombinations("2"))
