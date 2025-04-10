#importing word counting and character counting functions from stats.py
from stats import count_words_in_book
from stats import character_count

def main():
    book_path = "books/frankenstein.txt"
    print(f"{count_words_in_book(book_path)} words found in the document")
    characters = character_count(book_path)
    print(characters)

main()

