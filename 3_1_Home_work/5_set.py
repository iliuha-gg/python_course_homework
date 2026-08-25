# --------------- Task 5 ---------------


def set_union(first_set: set, second_set: set) -> set:
    """Return union of two sets."""
    return first_set | second_set


def is_subset(first_set: set[int], second_set: set[int]) -> bool:
    """Return True if the first set is a subset of the second set."""
    return first_set.issubset(second_set)


set_1 = {1, 2, 3}
set_2 = {3, 3, 4}

united_set = set_union(set_1, set_2)
print(united_set)

set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5}

print(is_subset(set_1, set_2))