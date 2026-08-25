# --------------- Task 6 ---------------


def print_is_even(num: int) -> None:
    """Define whether the number is even or odd."""
    print("Even" if num % 2 == 0 else "Odd")


def only_even_numbers(numbers: list[int]) -> list[int]:
    """Return only even numbers."""
    return [number for number in numbers if number % 2 == 0]


print_is_even(6)
print_is_even(7)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = only_even_numbers(my_list)
print(even_list)