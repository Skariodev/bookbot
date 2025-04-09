#Collection of functional functions:> 

#Function to turn book text into a long string
def get_book_text(filepath):
    with open(filepath) as f: 
        return f.read()

#function counting words in the book in filepath
def count_words_in_book(filepath):
    text = get_book_text(filepath)
    words_list = text.split()
    return len(words_list)
