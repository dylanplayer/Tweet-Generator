import random
import sys

def rearrange(words):
    random.shuffle(words)
    return words
    
if __name__ == '__main__':
    words = sys.argv[1:]
    shuffled_words = rearrange(words)
    print(shuffled_words)