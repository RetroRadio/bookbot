def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) 
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count(text)} words are contained in this book.")
    print(format_list(dict_list(char_count(text))))

def get_book_text(path): #opens text file
    with open(path) as f:
        return f.read()

def word_count(text): #counts the words by splitting on the whitespace
    return len(text.split())
    
def char_count(text): #commits each letter individually to a dictionary and updates the value each time the character is seen
    characters = {}
    for char in text.lower():
        characters[char] = characters.get(char, 0) + 1
    return characters

def dict_list(dict): #splits the dictionary into a list of dictionaries and sorts from highest to lowest value
    char_list = []
    for char, count in dict.items():
        if char.isalpha():
            char_data = {"char": char, "count": count}
            char_list.append(char_data)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict): #feeds the above function to sort by how many times a character has been seen
    return dict["count"]

def format_list(dict_list): #creates a new list with the sorted values formatted into a console readable form
    result = []
    for item in dict_list:
        char = item["char"]
        count = item["count"]
        result.append(f"The '{char}' character was found {count} times")
    return "\n".join(result) 

main()
