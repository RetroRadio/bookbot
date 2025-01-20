def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) 
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count(text)} words are contained in this book.")
    print(format_list(dict_list(char_count(text))))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())
    
def char_count(text):
    characters = {}
    for char in text.lower():
        characters[char] = characters.get(char, 0) + 1
    return characters

def dict_list(dict):
    char_list = []
    for char, count in dict.items():
        if char.isalpha():
            char_data = {"char": char, "count": count}
            char_list.append(char_data)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict):
    return dict["count"]

def format_list(dict_list):
    result = []
    for item in dict_list:
        char = item["char"]
        count = item["count"]
        result.append(f"The '{char}' character was found {count} times")
    return "\n".join(result) 

main()
