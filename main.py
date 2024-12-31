def main():
    with open("/home/lockenrocky/workspace/github.com/Lockenrocky/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    count_words(file_contents)
    print()
    count_characters(file_contents)

def count_words(file_contents):
    words = file_contents.split()
    print(f"{len(words)} words found in the document")

def count_characters(file_contents):
    characters = {}
    for letter in file_contents:
        l = letter.lower()
        if l.isalpha():
            if l in characters:
                characters[l] += 1
            else:
                characters[l] = 1
    sorted_characters = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
    for c in sorted_characters:
        print(f"The '{c}' character was found {sorted_characters[c]} times")

main()