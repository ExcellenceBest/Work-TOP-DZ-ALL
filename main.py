def find_enty(arr1, arr2):
    occurrences = {}
    for i in arr2:
        if i in arr1:
            occurrences[i] = occurrences.get(i, 0) + 1
    return occurrences

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [2, 4, 6, 8]
print(find_enty(arr1, arr2))