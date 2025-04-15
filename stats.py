from functools import wraps


def count_words(text: str) -> int:
    num_words = len(text.split())

    return num_words


def sort_dict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        dictionary = func(*args, **kwargs)
        sorted_dict = dict(sorted(dictionary.items(), reverse=True, key=lambda item: item[1]))

        return sorted_dict
    return wrapper


@sort_dict
def number_of_times_char_appears(text: str) -> dict:
    lower_case_text = text.lower()

    char_dict = {}

    for char in lower_case_text:
        if char not in char_dict:
            char_dict[char] = 1
        elif char in char_dict:
            char_dict[char] += 1

    return char_dict

