# --------------- Task 1 ---------------


def count_length(info: str) -> int:
    """Return the length of the element."""
    return len(info)


def strings_union(first_element: str, second_element: str) -> str:
    """Combine two strings."""
    return first_element + second_element


my_str = "hello world"
my_str1 = "hello"
my_str2 = ", world"

print(count_length(my_str))
print(strings_union(my_str1, my_str2))