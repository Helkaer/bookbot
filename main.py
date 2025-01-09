def main():
    path_to_file = "books/frankenstein.txt"
    text = get_text(path_to_file)
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    sorted_chars = characters_to_sorted_list(character_count)

    print(f"--- Begin report of {path_to_file}")
    print(f"Words found: {num_words}")
    print(f"Characters found:")
    for c in sorted_chars:
        if c["char"].isalpha():
            print(f"{c["char"]}:{c["num"]}")
    print("--- End Report ---")

def get_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_dict = {}
    lower_text = text.lower()
    for character in lower_text:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def characters_to_sorted_list(characters_dict):
    sorted_list = []
    for c in characters_dict:
        sorted_list.append({
            "char": c,
            "num": characters_dict[c]
        })
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]


main()