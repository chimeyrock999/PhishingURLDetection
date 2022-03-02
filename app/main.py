from flask import Flask
from flask import url_for
from flask import request
from flask import redirect
from collections import Counter
from flask import render_template
from flask.wrappers import Response
from . import predict

userAgent = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36')

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        url = request.form['txt_search']
        rs=predict.predict_new_url(url)
        print(rs)
        if (rs==1):
            return(render_template('phising_result.html'))
        if (rs==0):
            return (render_template('benign_result.html'))
        if (rs==-1):
            return (render_template('has_error.html'))
    return None


