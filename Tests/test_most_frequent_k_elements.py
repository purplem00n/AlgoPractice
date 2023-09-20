from Unit4PSE.most_frequent_k_elements import most_frequent_k_elements

def test_two_of_three_elements_returned():
    # arrange
    nums = [1,1,1,2,2,3]
    k = 2

    # act
    result = most_frequent_k_elements(nums, k)

    # assert
    assert result == [1, 2]

def test_single_element_returned():
 
    # arrange
    nums = [1]
    k = 1

    # act
    result = most_frequent_k_elements(nums, k)

    # assert
    assert result == [1]
    
def test_tied_most_frequent():
 
    # arrange
    nums = [1, 2]
    k = 1

    # act
    result = most_frequent_k_elements(nums, k)

    # assert
    assert result == [1] or result == [2]