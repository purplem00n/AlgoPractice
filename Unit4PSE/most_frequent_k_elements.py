def most_frequent_k_elements_original(arr, k):
    '''Return a k-length list of most freq elements in arr'''
    unique_numbers = {}
    for num in arr:
        unique_numbers[num] = unique_numbers.get(num, 0) + 1
    result = sorted(unique_numbers.keys(), key=lambda num: unique_numbers[num], reverse=True)
    # or key=counts.get
    return result[:k]

# Alternate solution using partitioning:

# can separate the freq mapping into another function to keep one job for one function

def partition_kth_value(arr, k, key):
    start = 0
    end = len(arr)

    if end - start <= 1:
        return
    
    # partition until the pivot ends up at k-1
    while True:
        pivot_idx = end - 1
        pivot = arr[pivot_idx]
        pivot_key = key(pivot) # uses the lambda function we defined

        left_list_end =  start
        

        for i in range(start, pivot_idx):
            element = arr[i]
            element_key = key(element)
            if element_key > pivot_key:
                arr[left_list_end], arr[i] = arr[i], arr[left_list_end] #swap values
                left_list_end += 1
            
        arr[left_list_end], arr[pivot_idx] = arr[pivot_idx], arr[left_list_end]

        # if we found the kth element, we know everything to the left is larger, can return
        if left_list_end == k - 1:
            break
        # if we're looking at an element smaller than k, need to continue to look to the right
        elif left_list_end < k:
            start = left_list_end + 1
        # if we're looking at an element smaller than k, need to keep looking to the left
        else:
            end = left_list_end



def most_frequent_k_elements(arr, k):
    '''Return a k-length list of most freq elements in arr'''
    unique_numbers = {}
    for num in arr:
        unique_numbers[num] = unique_numbers.get(num, 0) + 1

    uniques = list(unique_numbers)

    partition_kth_value(uniques, k, key=lambda num: unique_numbers[num])

    return uniques[:k]
