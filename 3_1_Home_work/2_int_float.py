# --------------- Task 2 ---------------


def squared_num(num: int) -> int:
    """Square number."""
    return num * num


def add_numbers(num_1: int, num_2: int) -> int:
    """Summarize a number."""
    return num_1 + num_2


def devide(num_1: int, num_2: int) -> tuple[int, int]:
    """Integer division."""
    return num_1 // num_2, num_1 % num_2


print(squared_num(2))
print(squared_num(3))
print(add_numbers(1, 2))

num_1 = 10
num_2 = 3

print(devide(num_1, num_2))