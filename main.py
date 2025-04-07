from stats import count_words, count_characters

def main():
    with open("/home/lockenrocky/workspace/github.com/Lockenrocky/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    count_words(file_contents)
    print()
    count_characters(file_contents)

main()