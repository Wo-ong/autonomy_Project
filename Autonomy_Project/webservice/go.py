from flask import Flask, render_template, request
import numpy as np


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/select')
def age():
    return render_template('ab.html')

@app.route('/select2')
def select2():
    return render_template('ab_2.html')

@app.route('/select3')
def select3():
    return render_template('ab_3.html')

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

@app.route('/predict', methods=['POST'])
def exercise_10():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['h']
    data9 = request.form['i']
    data10 = request.form['j']
    data11 = request.form['k']
    data12 = request.form['l']
    data13 = request.form['m']
    data14 = request.form['n']

    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14]])
    pred1 = ''.join(model_10_warmup.predict(arr))
    pred2 = ''.join(model_10_main.predict(arr))
    pred3 = ''.join(model_10_finish.predict(arr))
    return render_template('predict.html', res1 = pred1.split(':')[-1], res2 = ', '.join((pred2.split(':')[-1]).split(',')[:3]), res3 = pred3.split(':')[-1])


if __name__ == "__main__":
    app.run(debug=True)