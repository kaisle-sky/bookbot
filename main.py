
def count_words(text):
    words = text.split()
    print(len(words))


with open("./books/frankenstein.txt") as f:
    text_read = f.read()

count_words(text_read)