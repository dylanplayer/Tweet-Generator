import sys
import random

def get_words(number_of_words, filename='/usr/share/dict/words'):
    number_of_words = int(number_of_words)
    with open(filename, 'r') as dict:
        lines = [word.strip('\n') for word in dict]
        words = random.choices(lines, k=number_of_words)
        return words

if __name__ == '__main__':
    number_of_words = sys.argv[1]
    print(' '. join(get_words(number_of_words)))
    