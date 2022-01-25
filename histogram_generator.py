
PUNCTUATION = '''!()-[]{};:'"\,<>./?@#$%^&*_~”“'''

def histogram(filename='test_text.txt', type='d'):
    if type == 'd':
        histogram = {}
        words = []
        with open(filename, 'r') as text:
            for line in text:
                words += line.split()
            for raw_word in words:
                word = ''
                for char in raw_word.lower():
                    if char not in PUNCTUATION:
                        word += char
                if word in histogram.keys():
                    histogram[word] += 1
                else:
                    histogram.update({word: 1})
    elif type == 't':
        histogram = []
        words = []
        with open(filename, 'r') as text:
            for line in text:
                words += line.split()
            words.sort()
            for raw_word in words:
                word = ''
                for char in raw_word.lower():
                    if char not in PUNCTUATION:
                        word += char
                word_found = False
                for group in histogram:
                    if group[0] == word:
                        count = group[1] + 1
                        histogram.remove(group)
                        histogram.append((word, count))
                        word_found = True
                        break
                else:
                    histogram.append((word, 1))
    return histogram


def unique_words(histogram):
    return len(histogram)

def frequency(histogram, word):
    word = word.lower()
    if word in histogram:
        return histogram[word]
    else:
        return 0

if __name__ == '__main__':
    import time
    import math
    start = time.time()
    d_histogram = histogram(type='d')
    end = time.time()
    print('Time to create dict histogram', round((end - start) * 1000, 2), 'ms')
    print('Creating touple histogram...')
    start = time.time()
    t_histogram = histogram(type='t')
    end = time.time()
    print('Time to create touple histogram', round((end - start) * 1000, 2), 'ms')
    print('Unique words in histogram:', unique_words(d_histogram))
    print('Frequency of the in histogram', frequency(d_histogram, 'the'))
