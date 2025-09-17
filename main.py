from stats import word_count, char_count, sorted_char_count
import sys

# Returns text from book
def get_book_text(filepath):
    # Opens file
    with open(filepath) as file:
        # Reads content
        contents = file.read()

    # Returns file content
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    print(f"Found {word_count(book)} total words")
    sorted_char_count(char_count(book))

main()
