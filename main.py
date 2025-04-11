#Importing functoins from stats.py + sys module
from stats import count_words_in_book
from stats import character_count
from stats import sorted_characters
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words_in_book(sys.argv[1])} total words")
    print("--------- Character Count -------")
    characters = character_count(sys.argv[1])
    #print(f"dictionaries: {sorted_characters(book_path)}")
    for item in sorted_characters(sys.argv[1]):
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
main()