"""Count words in file."""
import sys
    
    
def tokenize(filename):
    words = []
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            word = line.split()
            words.extend(word)
    return words


def wordcount(tokenize):
    word_dict = {}
    for word in tokenize:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict


def print_word_counts(wordcount):
    for k, v in wordcount.items():
        print(k, v)



input_file = sys.argv[1]
words = tokenize(input_file)
count_words = wordcount(words)
print_word_counts(count_words)
