# --------------- Task 6 ---------------

from collections.abc import Callable


# Return "Even" for even numbers and "Odd" for odd numbers.
even_odd_check: Callable[[int], str] = (
    lambda number: "Even" if number % 2 == 0 else "Odd"  # noqa: E731
)

print(even_odd_check(6))
print(even_odd_check(7))