# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/7D5NNZWQ8Wr

# Brute force version
# Time Complexity O(N*K)
# Space Complexity O(1)


def find_averages_of_subarrays(K, arr):
    result = []
    for i in range(len(arr)-K+1):
        _sum = 0.0
        for j in range(i, i+K):
            _sum += arr[j]
        result.append(_sum/K)
    return result


def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
