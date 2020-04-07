# If a almost sorted_array only have two swaps, find them


def find_two_swapped(nums: List[int]) -> (int, int):
    n = len(nums)
    x = y = -1
    for i in range(n - 1):
        if nums[i + 1] < nums[i]:
            y = nums[i + 1]
            # first swap occurence
            if x == -1:
                x = nums[i]
            # second swap occurence
            else:
                break
    return x, y