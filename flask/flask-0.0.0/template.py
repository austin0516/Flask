#!flask/bin/python
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
#@app.route('/html_template')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
