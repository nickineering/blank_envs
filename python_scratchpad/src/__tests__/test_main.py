from src.main import get_second_small_num


def test_small_num():
    nums = [1, 2, 3, 4, 5]
    num = get_second_small_num(nums)
    assert num == 2


def test_wrong_order_small_num():
    nums = [7, 4, 1, 6, 2]
    num = get_second_small_num(nums)
    assert num == 2


def test_duplicate():
    nums = [3, 1, 1]
    num = get_second_small_num(nums)
    assert num == 3


def test_same_num_duplicate():
    nums = [1, 1, 1]
    num = get_second_small_num(nums)
    assert num is None


def test_one_small_num():
    nums = [1]
    num = get_second_small_num(nums)
    assert num is None
