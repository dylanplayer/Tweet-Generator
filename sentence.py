import sample

def get_sentance(filename, word_count):
  sentence_list = list(sample.sample(20, filename, type='s'))
  sentence_list[0] = sentence_list[0].upper()
  sentence_list.append('.')
  sentence = ''.join(sentence_list)
  return sentence
