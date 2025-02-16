from copy import copy


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_text_lower = copy(book_text).lower()
    word_count = len(book_text_lower.split())
    chars_dict = get_chars_dict(book_text_lower)
    sorted_chars_dict = sort_dict_g_to_l(chars_dict)

    print(f"\n--- Begin report of {book_path} ---\n")
    print(f"{word_count:,} words found in the document\n")

    for k, v in sorted_chars_dict.items():
        print(f"The '{k}' charcter was found {v} times")

    print("\n--- End report ---\n")


def get_book_text(book_path):
    with open(book_path, "r") as f:
        file_contents = f.read()
    return file_contents


def get_chars_dict(text):
    char_count_dict = {}
    for char in text:
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1
    return char_count_dict


def sort_dict_g_to_l(dictionary):
    sort_chars_dict = {}
    for key, value in dictionary.items():
        if key.isalpha():
            sort_chars_dict[key] = value

    sorted_dict = dict(sorted(sort_chars_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


if __name__ == "__main__":
    main()
