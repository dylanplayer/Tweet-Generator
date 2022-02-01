from flask import Flask, render_template
import sample
import os

app = Flask(__name__)
TEXT_FILE = 'musk.txt'

@app.route('/')
def index():
  return render_template('index.html', title='Musk Tweet', generated_text=sample.sample(20, TEXT_FILE, type='s'))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='3000', debug=True)