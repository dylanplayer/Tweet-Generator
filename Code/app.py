from flask import Flask, render_template
from tokens import tokenize
from dictogram import Dictogram
from sentence import get_sentance, create_markov, create_histogram
from markov import Markov

app = Flask(__name__)
TEXT_FILE = 'data/sample.txt'
words = tokenize(TEXT_FILE)
histogram = create_histogram(words)
markov = Markov(histogram, words)

@app.route('/')
def index():
  return render_template('index.html', title='Musk Tweet', generated_text=get_sentance(histogram, markov, 5))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='3000', debug=True)
