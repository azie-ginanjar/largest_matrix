def largest_matrix(arr):
    # Write your code here
    if len(arr) == 0 or len(arr[0]) == 0:
        return 0

    cache = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]

    for i in range(len(arr)):
        cache[i][0] = arr[i][0]

    for j in range(len(arr[0])):
        cache[0][j] = arr[0][j]

    largest_size = 0

    for i in range(1, len(arr)):
        for j in range(1, len(arr[i])):
            if arr[i][j] == 1 and arr[i - 1][j] == 1 and arr[i][j - 1] == 1 and arr[i - 1][j - 1] == 1:
                cache[i][j] = min(cache[i - 1][j], cache[i][j - 1], cache[i - 1][j - 1]) + 1
            else:
                cache[i][j] = arr[i][j]

            largest_size = max(largest_size, cache[i][j])

    return largest_size
