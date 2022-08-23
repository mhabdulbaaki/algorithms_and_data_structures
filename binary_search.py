def binary_search(arr, item):
    """takes a sorted list and the item to search for"""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if item > guess:
            low = mid + 1
        else:
            high = mid - 1
    return None


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 6))
