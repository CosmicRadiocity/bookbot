def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        words = word_count(file_contents)
        print(f"Words: {words}")

def word_count(txt):
    words = txt.split()
    return len(words)

main()