import requests
def count_unique_words(url):
    book = requests.get(url)
    lines = book.text.split("\n")
    punctuation_remove = ",.:!?;"
    punctuation_space = "'\"()[]-_"

    unique_words = {}

    for line in lines:
        for c in punctuation_remove:
            line = line.replace(c, "")
        for c in punctuation_space:
            line = line.replace(c, " ")

        words = line.split()
        for word in words:
            word = word.lower()
            unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words


book1_url = 'https://www.gutenberg.org/cache/epub/2554/pg2554.txt'  # Crime and Punishment by Fyodor Dostoevsky
book2_url = 'https://www.gutenberg.org/cache/epub/2641/pg2641.txt'  # A Room with a View by E.M. Forster

unique_words_book1 = count_unique_words(book1_url)
unique_words_book2 = count_unique_words(book2_url)

print(f"Number of unique words in Book 1 (Crime and Punishment): {len(unique_words_book1)}")
print(f"Number of unique words in Book 2 (A Room with a View): {len(unique_words_book2)}")

if len(unique_words_book1) > len(unique_words_book2):
    print("Fyodor Dostoevsky used more unique words in 'Crime and Punishment'.")
elif len(unique_words_book1) < len(unique_words_book2):
    print("E.M. Forster used more unique words in 'A Room with a View'.")
else:
    print("Both authors used the same number of unique words.")