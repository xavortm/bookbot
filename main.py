import sys

from stats import get_format_dict, get_num_words, get_characters_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")

    path = sys.argv[1]
    book_contents = get_book_text(path)
    num_words = get_num_words(book_contents)
    chars_dict = get_characters_count(book_contents)
    sorted = get_format_dict(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted:
        if str(item["char"]).isalpha():
            print(f"{item['char']}: {item['num']}")

main()
