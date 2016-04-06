def flatten(arr):
    result = []
    if isinstance(arr, list):
        for i in arr:
            result.extend(flatten(i))
    else:
        result.append(arr)
    return result


l = [[1, 2, 3], [4, 5, 6], 7, [7], [8, [2, [2, 54, 3]], 9]]

print flatten(l)
