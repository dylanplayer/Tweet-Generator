import enchant

PUNCTUATION = '''!()-[]{};:'"\…,<>./?@#$%‼^&*_~”„“‥'''
d = enchant.Dict("en_US")

def histogram(filename='test_text.txt', type='d', sample=[]):
    words = sample
    if not len(words) > 0:
        with open(filename, 'r') as text:
                for raw_line in text:
                    line = ''
                    for char in raw_line:
                        if char not in PUNCTUATION:
                            line += char
                    words += line.lower().split()
    if type == 'd':
        histogram = {}
        for word in words:
            if word in histogram.keys():
                histogram[word] += 1
            else:
                if d.check(word):
                    histogram.update({word: 1})
    elif type == 't':
        histogram = []
        words.sort()
        index = -1
        for word in words:
            if len(histogram) != 0 and word == histogram[index][0]:
                count = histogram[index][1] + 1
                del histogram[-1]
                histogram.append((word, count))
            else:
                histogram.append((word, 1))
                index += 1
    return histogram

def unique_words(histogram):
    return len(histogram)

def frequency(histogram, word):
    word = word.lower()
    if isinstance(histogram, dict):
        if word in histogram:
            return histogram[word]
    elif isinstance(histogram, list):
        for group in histogram:
            if group[0] == word:
                return group[1]
    return 0

def buildJSON(histogram):
    import json
    with open('results.json', 'w') as output:
        words = []
        if isinstance(histogram, dict):
            for key, value in histogram.items():
                group = {
                    'word': key,
                    'amount': value
                }
                words.append(group)
        elif isinstance(histogram, list):
            for ele in histogram:
                group = {
                    'word': ele[0],
                    'amount': ele[1]
                }
                words.append(group)
        output.write(json.dumps(words))

if __name__ == '__main__':
    import time
    import math
    start = time.time()
    d_histogram = histogram(type='d')
    end = time.time()
    print('Time to create dict histogram', round((end - start) * 1000, 2), 'ms')
    start = time.time()
    t_histogram = histogram(type='t')
    end = time.time()
    print('Time to create touple histogram', round((end - start) * 1000, 2), 'ms')
    print('Unique words:', unique_words(d_histogram))
    print('"the" :', frequency(d_histogram, 'the'))
    buildJSON(t_histogram)
