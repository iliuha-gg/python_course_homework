# --------------- Task 3 ---------------


def find_average(nums: list[int]) -> float:
    """Find average of numbers."""
    return sum(nums) / len(nums)


def get_same_element(
    first_element: list[int],
    second_element: list[int],
) -> list[int]:
    """Return list with same elements."""
    return list(set(first_element) & set(second_element))

my_list = [1, 2, 3, 4, 5, 6]
num_list_1 = [1, 2, 3]
num_list_2 = [3, 2, 6]

print(find_average(my_list))
print(get_same_element(num_list_1, num_list_2))