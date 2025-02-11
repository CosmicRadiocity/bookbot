def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        ##print(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        words = word_count(file_contents)
        print(f"{words} words found in the document\n")
        characters = sort_dict(character_count(file_contents))
        for char in characters:
            if char["char"].isalpha():
                print(f"the '{char["char"]}' was found {char["num"]} times")
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

def sort_on(dict):
    return dict['num']

def sort_dict(dict):
    res = []
    for item in dict:
        res.append({"char": item, "num":dict[item]})
    res.sort(reverse=True, key=sort_on)
    return res

main()