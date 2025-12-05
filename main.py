import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(text: str) -> str:
    with open(text, 'r') as f:
        file_contents = f.read()
    return file_contents

def print_report(text: str):
    char_counts = get_char_counts(text)
    sorted_counts = sort_char_counts(char_counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words(text)
    print("--------- Character Count -------")
    for item in sorted_counts:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def main() -> None:
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    print_report(book_text)

main()