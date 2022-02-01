import re

def cleaner(filename):
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

if __name__ == '__main__':
  cleaner('musk.txt')
