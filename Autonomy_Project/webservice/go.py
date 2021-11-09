from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__)

model_10_warmup = pickle.load(open('10_warmup.pkl', 'rb'))
model_10_main = pickle.load(open('10_main.pkl', 'rb'))
model_10_finish = pickle.load(open('10_finish.pkl', 'rb'))

model_20_warmup = pickle.load(open('20_warmup.pkl', 'rb'))
model_20_main = pickle.load(open('20_main.pkl', 'rb'))
model_20_finish = pickle.load(open('20_finish.pkl', 'rb'))

model_60_warmup = pickle.load(open('60_warmup.pkl', 'rb'))
model_60_main = pickle.load(open('60_main.pkl', 'rb'))
model_60_finish = pickle.load(open('60_finish.pkl', 'rb'))


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/select')
def age():
    return render_template('ab.html')

@app.route('/input10')
def input10():
    return render_template('input_10.html')

@app.route('/input20')
def input20():
    return render_template('input_20.html')

@app.route('/input60')
def input60():
    return render_template('input_60.html')

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


@app.route('/predict', methods=['POST'])
def exercise_20():
    data21 = request.form['aa']
    data22 = request.form['bb']
    data23 = request.form['cc']
    data24 = request.form['dd']
    data25 = request.form['ee']
    data26 = request.form['ff']
    data27 = request.form['gg']
    data28 = request.form['hh']
    data29 = request.form['ii']
    data30 = request.form['jj']
    data31 = request.form['kk']
    data32 = request.form['ll']

    arr = np.array([[data21, data22, data23, data24, data25, data26, data27, data28, data29, data30, data31, data32]])
    pred1 = ''.join(model_20_warmup.predict(arr))
    pred2 = ''.join(model_20_main.predict(arr))
    pred3 = ''.join(model_20_finish.predict(arr))
    return render_template('predict.html', res1=pred1, res2=pred2, res3=pred3)


@app.route('/predict', methods=['POST'])
def exercise_60():
    data01 = request.form['aaa']
    data02 = request.form['bbb']
    data03 = request.form['ccc']
    data04 = request.form['ddd']
    data05 = request.form['eee']
    data06 = request.form['fff']
    data07 = request.form['ggg']
    data08 = request.form['hhh']
    data09 = request.form['iii']
    data010 = request.form['jjj']
    data011 = request.form['kkk']
    data012 = request.form['lll']
    data013 = request.form['mmm']

    arr = np.array([[data01, data02, data03, data04, data05, data06, data07, data08, data09, data010, data011, data012, data013]])
    pred_1 = ''.join(model_60_warmup.predict(arr))
    pred_2 = ''.join(model_60_main.predict(arr))
    pred_3 = ''.join(model_60_finish.predict(arr))
    return render_template('predict.html', res1 = pred_1, res2 = pred_2, res3 = pred_3)


@app.route('/predict', methods=['POST'])
def nickname():
    nickname = request.form['nickname']
    return render_template('predict.html', nickname = nickname)

if __name__ == "__main__":
    app.run(debug=True)