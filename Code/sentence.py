from dictogram import Dictogram

PUNCTUATION = '''!()-[]{};:'"\…,<>./?@#$%‼^&*_~”„“‥'''

def get_sentance(filename, word_count):
  words_list = get_words_list(filename)
  histogram = Dictogram(word_list=words_list)
  sentence_list = []
  for word in range(word_count):
    sentence_list.append(histogram.sample())
  sentence_list.append('.')
  sentence = ' '.join(sentence_list)
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
