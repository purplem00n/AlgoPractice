def most_frequent_k_elements(arr, k):
    '''Return a k-length list of most freq elements in arr'''
    unique_numbers = {}
    for num in arr:
        unique_numbers[num] = unique_numbers.get(num, 0) + 1
    result = sorted(unique_numbers.keys(), key=lambda num: unique_numbers[num], reverse=True)
    return result[:k]