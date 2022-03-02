import sys

PUNCTUATION = '''!()-[]{};:'"\…,<>./?@#$%‼^&*_~”„“‥'''

def tokenize(filename='./data/sample.txt'):
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

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(tokenize(sys.argv[1]))
    else:
        print(tokenize())
