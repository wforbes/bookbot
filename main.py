from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text() -> str:
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
    return file_contents

def main() -> None:
    book_text = get_book_text()
    char_counts = get_char_counts(book_text)
    sorted_counts = sort_char_counts(char_counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words(book_text)
    print("--------- Character Count -------")
    for item in sorted_counts:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()