from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/app')
def blog():
    return "Hello, from App path!"

@app.route('/myname')
def myname():
    return "My name is Robert Berry"

@app.route('/<page>')
def default(page):
  response = make_response('The page %s does not exist.' % page, 404)
  return response

if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=3000)
