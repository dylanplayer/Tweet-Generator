from dictogram import Dictogram

class Markov(dict):
  def __init__(self, histogram, word_list):
    super(Markov, self).__init__()
    self.types = 0
    self.tokens = 0
    for current_word in histogram:
      following_words = []
      for i in range(len(word_list)):
        if word_list[i] == current_word and i + 1 < len(word_list):
          following_words.append(word_list[i+1])
      following_words_histogram = Dictogram(following_words)
      self.update({current_word: following_words_histogram})
  
  def get_following_words(self, word):
    return list(self[word].keys())

  def get_folllowing_words_counts(self, word):
    return list(self[word].values())

  def get_following_words_dictogram(self, word):
    return self[word]

if __name__ == '__main__':
  PUNCTUATION = '''!()-[]{};:'"\…,<>./?@#$%‼^&*_~”„“‥'''
  words = []
  with open('./data/sample.txt', 'r') as text:
    for raw_line in text:
      line = ''
      for char in raw_line:
        if char not in PUNCTUATION:
          line += char
      words += line.lower().split()
  histogram = Dictogram(words)
  markov = Markov(histogram, words)
  print(markov.get_following_words_dictogram('the'))