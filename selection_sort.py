def find_smallest(arr):
    """takes an array and return the index of the smallest element"""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def sort_items(arr, asc=True):
    """returns a sorted item. Order is by default ascending but can be changed by the asc field"""
    new_array = []
    if asc:
        for i in range(len(arr)):
            item = arr.pop(find_smallest(arr))
            new_array.append(item)
    else:
        for i in range(len(arr)):
            item = arr.pop(find_smallest(arr))
            new_array.insert(0, item)
    return new_array


sorted_result = sort_items(arr=[120, 1, 22, 11, -34, 50, 2, 5, 3, 6, 77, 0])
print(f"sorted results: {sorted_result}")


sorted_result = sort_items(arr=[120, 1, 22, 11, -34, 50, 2, 5, 3, 6, 77, 0], asc=False)
print(f"sorted results: {sorted_result}")
