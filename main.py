
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(list):
    big_string = "".join(list)
    little_string = big_string.lower()
    letter_dict = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0,
        "h" : 0,
        "i" : 0,
        "j" : 0,
        "k" : 0,
        "l" : 0,
        "m" : 0,
        "n" : 0,
        "o" : 0,
        "p" : 0,
        "q" : 0,
        "r" : 0,
        "s" : 0,
        "t" : 0,
        "u" : 0,
        "v" : 0,
        "w" : 0,
        "x" : 0,
        "y" : 0,
        "z" : 0
    }
    for n in range(0, len(little_string)):
        check = little_string[n]
        if check in letter_dict:
            letter_dict[check] += 1
    return letter_dict

def book_report(book):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(book)} words found in the document")
    print("")
    sorted_book = sorted(count_letters(book).items(), key=lambda x:x[1], reverse=True)
    converted_dict = dict(sorted_book)
    for key in converted_dict:
        print(f"The '{key}' character was found {converted_dict[key]} times")
    print("--- End report ---")


with open("./books/frankenstein.txt") as f:
    text_read = f.read()

book_report(text_read)