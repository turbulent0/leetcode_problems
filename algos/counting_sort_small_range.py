def countingSort(arr):
    # Find the maximum element in the array
    max_val = max(arr)

    # Create a counting array of size max_val + 1
    count = [0] * (max_val + 1)

    # Count the occurrences of each element
    for num in arr:
        count[num] += 1

    # Calculate the cumulative sum of the count array
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    print('cum count',  count)
    # Create a new array to store the sorted elements
    sorted_arr = [0] * len(arr)

    # Place the elements in sorted order using the count array
    for num in arr:
        sorted_arr[count[num] - 1] = num
        count[num] -= 1

    return sorted_arr

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = countingSort(arr)
print(sorted_arr)
