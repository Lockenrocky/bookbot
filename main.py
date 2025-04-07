import sys
from stats import count_words, count_characters

def main():
    #with open("/home/lockenrocky/workspace/github.com/Lockenrocky/bookbot/books/frankenstein.txt") as f:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    with open("/home/lockenrocky/workspace/github.com/Lockenrocky/bookbot/" + sys.argv[1]) as f:
        file_contents = f.read()
    count_words(file_contents)
    print()
    count_characters(file_contents)

main()