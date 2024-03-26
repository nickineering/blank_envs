def get_second_small_num(nums: list[int]):
    nums_set = set(nums)
    if len(nums_set) < 2:
        return None
    nums_result = sorted(nums_set)
    return nums_result[1]


if __name__ == "__main__":
    pass
