from flask import render_template
from flask import Flask
from flask import make_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/myname')
def myname():
    return "My name is Robert Berry"

@app.route('/<page>')
def default(page):
  response = make_response('The page %s does not exist.' % page, 404)
  return response

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
