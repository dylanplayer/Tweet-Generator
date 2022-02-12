from markov import Markov
from dictogram import Dictogram

PUNCTUATION = '''!()-[]{};:'"\…,<>./?@#$%‼^&*_~”„“‥'''

def get_sentance(filename, word_count):
  words_list = get_words_list(filename)
  histogram = Dictogram(word_list=words_list)
  markov = Markov(histogram, words_list)
  sentence_list = []
  sentence_list.append(histogram.sample())
  for count in range(1, word_count):
    word = markov.get_following_words_dictogram(sentence_list[count-1]).sample()
    sentence_list.append(word)
  sentence = ' '.join(sentence_list)
  sentence += '.'
  return sentence

def get_words_list(filename):
  words = []
  with open(filename, 'r') as text:
    for raw_line in text:
      line = ''
      for char in raw_line:
        if char not in PUNCTUATION:
          line += char
      words += line.lower().split()
  return words

if __name__ == '__main__':
  sentence = get_sentance('./data/sample.txt', 10)
  print(sentence)
