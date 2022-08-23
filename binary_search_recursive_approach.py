def binary_search_recursive(arr: list, target: int):
    mid_point = len(arr) // 2

    if len(arr) == 0:
        return False

    if arr[mid_point] == target:
        return True

    if arr[mid_point] > target:
        return binary_search_recursive(arr=arr[:mid_point], target=target)

    elif arr[mid_point] < target:
        return binary_search_recursive(arr=arr[mid_point + 1:], target=target)

    else:
        return False


print(binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8], -6))
