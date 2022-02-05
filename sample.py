from sys import argv
import tokens
import random

def sample(length, filename='test_text.txt', type='l', histogram=None):
  sample = []
  if histogram == None:
    histogram = tokens.histogram(filename)
  words = list(histogram.keys())
  weights = list(histogram.values())
  for i in range(length):
    total_words = sum(weights)
    random_number = random.randint(0, total_words)
    count = 0
    for index, weight in enumerate(weights):
      count += weight
      if random_number <= count:
        sample.append(words[index])
        break
  if type == 'l':
    return sample
  elif type == 's':
    return ' '.join(sample)

def test_sample(size, filename='test_text.txt', word='the'):
  my_sample = sample(size)
  sample_histogram = tokens.histogram(filename, sample=my_sample)
  control_histogram = tokens.histogram(filename)
  print('Frequency of:', word)
  print('Sample: ', frequency_percentage(sample_histogram, word))
  print('Control: ', frequency_percentage(control_histogram, word))

def frequency_percentage(histogram, word):
  size = sum(list(histogram.values()))
  frequency = str((tokens.frequency(histogram, word) / size) * 100) + '%'
  return frequency

if __name__ == '__main__':
  # sample_length = int(argv[1])
  # my_sample = sample(sample_length)
  # print(' '.join(my_sample))
  test_sample(100000, word='at')
