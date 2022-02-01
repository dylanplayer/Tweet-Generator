from sys import argv
import histogram_generator
import random

def sample(length, filename='test_text.txt', type='a'):
  # sample = random.choices(words, weights, k=length)
  sample = []
  histogram = histogram_generator.histogram(filename)
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
  if type == 'a':
    return sample
  elif type == 's':
    return ' '.join(sample)

def test_sample(size, filename='test_text.txt', word='the'):
  my_sample = sample(size)
  sample_histogram = histogram_generator.histogram(filename, sample=my_sample)
  control_histogram = histogram_generator.histogram(filename)
  print('Frequency of:', word)
  print('Sample: ', str((histogram_generator.frequency(sample_histogram, word) / size) * 100) + '%')
  print('Control: ', str((histogram_generator.frequency(control_histogram, word) / sum(list(control_histogram.values()))) * 100) + '%')

if __name__ == '__main__':
  # sample_length = int(argv[1])
  # my_sample = sample(sample_length)
  # print(' '.join(my_sample))
  test_sample(100000, word='the')
