# --------------- Task 4 ---------------


def find_key(data: dict) -> None:
    """Find key values from dict."""
    for key in data:
        print(key)


def dict_union(first_dict: dict, second_dict: dict) -> dict:
    """Return combined dict."""
    return first_dict | second_dict


my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

dict_1 = {"a": 1, "b": 2}
dict_2 = {"c": 3, "d": 4}

find_key(my_dict)

dict_3 = dict_union(dict_1, dict_2)
print(dict_3)