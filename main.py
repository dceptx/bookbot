from stats import *
from sys import argv


if len(argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)
else:
    book_path = argv[1]


def get_book_text(file_path: str) -> str:
    with open(file_path, 'r') as f:
        file_contents = f.read()

    return file_contents


def main():
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    characters = number_of_times_char_appears(book_text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for c, v in characters.items():
        if c.isalpha():
            print(f"{c}: {v}")

    print("============= END ===============")


if __name__ == '__main__':
    main()

