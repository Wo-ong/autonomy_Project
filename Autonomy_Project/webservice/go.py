from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/select')
def select():
    return render_template('ab.html')

@app.route('/select2')
def select2():
    return render_template('ab_2.html')

@app.route('/select3')
def select3():
    return render_template('ab_3.html')

@app.route('/select3_60')
def select3_60():
    return render_template('ab_3_60.html')

@app.route('/wait')
def wait():
    return render_template('wait.html')

@app.route('/input10')
def input10():
    return render_template('input_10.html')

@app.route('/input20')
def input20():
    return render_template('input_20.html')

@app.route('/input60')
def input60():
    return render_template('input_60.html')

@app.route('/predict_ex')
def predict_ex():
    return render_template('predict_ex.html')

if __name__ == "__main__":
    app.run(debug=True)