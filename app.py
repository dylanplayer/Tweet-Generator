from flask import Flask, render_template
import sentence as sentence
import os

app = Flask(__name__)
TEXT_FILE = 'data/sample.txt'

@app.route('/')
def index():
  return render_template('index.html', title='Musk Tweet', generated_text=sentence.get_sentance(TEXT_FILE, 20))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='3000', debug=True)