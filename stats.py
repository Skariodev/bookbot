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

def character_count(filepath):
    text = get_book_text(filepath)
    all_characters = {}
    for character in text.lower():
        if character not in all_characters:
            all_characters[character] = 1
        else:
            all_characters[character] += 1
    return all_characters

def sort_on(dict):
    return dict["num"]

def sorted_characters(filepath): 
    unsorted_list = character_count(filepath)
    dict_list = []

    for character in unsorted_list:
        if character.isalpha():
            dict = {"char": character, "num": unsorted_list[character]}
            dict_list.append(dict)
    
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list