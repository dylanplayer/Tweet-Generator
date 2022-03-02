from os.path import exists
import json
from tokens import tokenize
from dictogram import Dictogram

class Markov(dict):
  def __init__(self, histogram, word_list):
    super(Markov, self).__init__()
    if exists('./markov.json'):
      loaded_markov = Markov.load()
      for key, value in loaded_markov.items():
        self.update({key: Dictogram(dict=value)})
    else:
      for current_word in histogram:
        following_words = []
        for i in range(len(word_list)):
          if word_list[i] == current_word and i + 1 < len(word_list):
            following_words.append(word_list[i+1])
        following_words_histogram = Dictogram(following_words)
        self.update({current_word: following_words_histogram})
      self.save()
    
  def save(markov):
    with open('markov.json', 'w') as file:
      json.dump(markov, file)

  def load():
    with open('markov.json', 'r') as file:
      return json.load(file)
  
  def get_following_words(self, word):
    return list(self[word].keys())

  def get_folllowing_words_counts(self, word):
    return list(self[word].values())

  def get_following_words_dictogram(self, word):
    return self[word]

if __name__ == '__main__':
  words = tokenize()
  histogram = Dictogram(words)
  markov = Markov(histogram, words)
