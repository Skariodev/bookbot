#importing word counting and character counting functions from stats.py
from stats import count_words_in_book
from stats import character_count
from stats import sorted_characters

def main():
    book_path = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words_in_book(book_path)} total words")
    print("--------- Character Count -------")
    characters = character_count(book_path)
    #print(characters)
    #Print the line below by accessing the key:value pairs, should not print "char" and "num" dummy.
    #print(f"dictionaries: {sorted_characters(book_path)}")
    for item in sorted_characters(book_path):
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
main()