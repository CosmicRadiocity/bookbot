def main():
    alphabet = []
    with open("books/alphabet.txt") as f:
        alphabet = f.read().split()
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        ##print(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        words = word_count(file_contents)
        print(f"{words} words found in the document\n")
        characters = character_count(file_contents)
        for char in characters:
            if char in alphabet:
                print(f"the '{char}' was found {characters[char]} times")
        print("--- End report ---")


def word_count(txt):
    words = txt.split()
    return len(words)

def character_count(txt):
    res = {}
    for char in txt:
        char = char.lower()
        if char in res:
            res[char] += 1
        else:
            res [char] = 1
    return res

main()