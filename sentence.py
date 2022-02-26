from markov import Markov
from dictogram import Dictogram

PUNCTUATION = '''!()-[]{};:'"\…,<>./?@#$%‼^&*_~”„“‥'''

def get_sentance(histogram ,markov, k):
  sentence_list = []
  sentence_list.append(histogram.sample())
  for count in range(1, k):
    word = markov.get_following_words_dictogram(sentence_list[count-1]).sample()
    sentence_list.append(word)
  sentence = ' '.join(sentence_list)
  sentence += '.'
  return sentence

def get_words_list(filename):
  print('Creating Words List')
  words = []
  with open(filename, 'r') as text:
    for raw_line in text:
      line = ''
      for char in raw_line:
        if char not in PUNCTUATION:
          line += char
      words += line.lower().split()
  words = [words[i] + " " + words[i+1] + " " + words[i+2] + " " + words[i+3] for i in range(0, len(words)-3, 4)]
  print('Words List Done')
  return words

def create_histogram(words):
  print('Creating Histogram')
  histogram = Dictogram(words)
  print('Histogram Done')
  return histogram

def create_markov(histogram, words):
  print('Creating Markov')
  markov = Markov(histogram, words)
  print('Markov Done')
  return markov

if __name__ == '__main__':
  words_list = get_words_list('./data/sample.txt')
  words_list = [words_list[i] + " " + words_list[i+1] for i in range(0, len(words_list)-1, 2)]
  histogram = Dictogram(word_list=words_list)
  markov = Markov(histogram, words_list)
  sentence = get_sentance(markov, 5)
  print(sentence)
  sentence = get_sentance(markov, 5)
  print(sentence)
