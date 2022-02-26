import re
import enchant

def cleaner(filename):
  d = enchant.Dict("en_US")
  tweets = []
  with open(filename, 'r') as data:
    for tweet in data:
      temp = re.sub("@[A-Za-z0-9]+","",tweet)
      temp = re.sub("#[A-Za-z0-9_]+","", temp)
      temp = re.sub(r"http\S+", "", temp)
      temp = re.sub(r"www.\S+", "", temp)
      tweets.append(temp)
  with open(filename, 'w') as data:
    for tweet in tweets:
      data.write(tweet)
  words = []
  with open(filename, 'r') as text:
          for raw_line in text:
              line = ''
              for char in raw_line:
                    line += char
              words += line.lower().split()
  with open(filename, 'w') as data:
    for word in words:
      if d.check(word):
        data.write(word + ' ')

if __name__ == '__main__':
  cleaner('data/sample.txt')
