from typing import List, Dict

# Returns word count
def word_count(text: str) -> int:
    words: List[str] = text.split()
    count: int = 0

    # Go through each word in the list and update count
    for word in words:
        count += 1

    # Return count
    return count

# Returns a dictionary of the count of each character
def char_count(text: str) -> Dict:
    char_dict: Dict = {}

    # Splits text into characters
    split_text: List[str] = list(text)

    for char in split_text:
        char = char.lower()
        if char not in char_dict:
            char_dict.update({char: 1})
        else: char_dict[char] += 1

    return char_dict

# Helper function
def sort_num(chars: Dict) -> List[Dict]:
    return chars["num"]

 # Returns sorted list of word count
def sorted_char_count(dict: Dict) -> None:
    new_dict: List[Dict] = []

    for item in dict:
        if item.isalpha():
            new_dict.append({ "char": item, "num": dict[item] })
        else: continue

    new_dict.sort(reverse=True, key=sort_num)

    for item in new_dict:
        print(f"{item['char']}: {item['num']}")
