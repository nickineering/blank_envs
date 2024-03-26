import math


def get_second_small_num_old(nums: list[int]):
    nums_set = set(nums)
    if len(nums_set) < 2:
        return None
    nums_result = sorted(nums_set)
    return nums_result[1]


def get_second_small_num(nums: list[int]) -> float | int | None:
    first = math.inf
    second = math.inf
    for num in nums:
        if num < first:
            second = first
            first = num
        elif num < second and num != first:
            second = num

    if second == math.inf:
        second = None
    return second


if __name__ == "__main__":
    pass
