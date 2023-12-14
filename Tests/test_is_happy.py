from LeetCode.isHappy import is_happy, isHappy

def test_19_returns_true():
    # arrange
    n = 19

    # act
    result = is_happy(n)

    # assert
    assert result is True

def test_2_returns_false():
    # arrange
    n = 2

    # act
    result = is_happy(n)

    # assert
    assert result is False

def test_19_returns_true_recursively():
    # arrange
    n = 19

    # act
    result = isHappy(n)

    # assert
    assert result is True

def test_2_returns_false_recursively():
    # arrange
    n = 2

    # act
    result = isHappy(n)

    # assert
    assert result is False