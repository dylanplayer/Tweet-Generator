from crypt import methods
from flask import Flask, redirect, render_template, request
from twitter import tweet
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

@app.route('/tweet', methods=['POST'])
def create_tweet():
  tweet(request.form['sentence'])
  return redirect('/')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='3000', debug=True)
