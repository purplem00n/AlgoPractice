from Unit4PSE.arr_to_bst import arr_to_bst

def test_will_return_balanced_bst_for_odd_lengthed_list():
    # Arrange
    arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]

    # Act
    result = arr_to_bst(arr)

    # Assert
    assert result.val == 25

def test_will_return_none_for_empty_list():
    # Arrange
    arr = []

    # Act
    result = arr_to_bst(arr)

    # Assert
    assert result is None