#importing word counting function from stats.py
from stats import count_words_in_book

def main():
    book_path = "books/frankenstein.txt"
    print(f"{count_words_in_book(book_path)} words found in the document")

main()

