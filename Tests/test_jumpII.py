from LeetCode.jumpII import jump

def test_decending_order():
    # arrange
    nums = [10,9,8,7,6,5,4,3,2,1,1,0]

    # act
    result = jump(nums)

    # assert
    assert result == 2

def test_best_choice_not_largest():
        # arrange
    nums = [8, 3, 4, 9, 5, 9, 3, 5, 7, 2, 4, 5, 3, 2, 0, 1]

    # act
    result = jump(nums)

    # assert
    assert result == 2