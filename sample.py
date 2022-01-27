from sys import argv
import histogram_generator
import random

def sample(length, filename='test_text.txt'):
  histogram = histogram_generator.histogram(filename)
  words = list(histogram.keys())
  weights = list(histogram.values())
  sample = random.choices(words, weights, k=length)
  return sample

def test_sample(size, filename='test_text.txt', word='the'):
  my_sample = sample(size)
  sample_histogram = histogram_generator.histogram(filename, sample=my_sample)
  control_histogram = histogram_generator.histogram(filename)
  print('Frequency of:', word)
  print('Sample: ', histogram_generator.unique_words(sample_histogram))
  print('Control: ', histogram_generator.unique_words(control_histogram))

if __name__ == '__main__':
  # import sys
  # sample_length = int(argv[1])
  # my_sample = sample(sample_length)
  # print(' '.join(my_sample))
  test_sample(100000, word='gatsby')
