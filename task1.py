def sort_unique_array(array):
    unique_numbers = set(array)
    unique_sorted_numbers_list = sorted(list(unique_numbers))
    return unique_sorted_numbers_list


arr = [-7, 133, 14, 99, 3, 5, 0, -22, 17, -17, 3, 14, 5, 7]
print(sort_unique_array(arr))
