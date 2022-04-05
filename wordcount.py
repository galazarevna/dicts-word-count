"""Count words in file."""
import sys


def tokenize(filename):
    all_words = []
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            words = line.split()
            for i in range(len(words)):
                words[i] = words[i].lower()
                for letter in words[i]:
                    if letter in punc:
                        words[i] = words[i].replace(letter, "")
            all_words.extend(words)
    return all_words


def wordcount(tokenize):
    word_dict = {}
    for word in tokenize:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict


def print_word_counts(wordcount):
    for k, v in wordcount.items():
        print(k, v)


input_file = sys.argv[1]
tokens = tokenize(input_file)
count_words = wordcount(tokens)
print_word_counts(count_words)
