from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///USERS_20.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class input1(db.Model):
    __tablename__ = 'User_20_1'
    id = db.Column(db.String, primary_key=True)
    password = db.Column(db.Integer, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    sex = db.Column(db.Integer, nullable=True)

    def __init__(self, id, password, age, sex):
        self.id = id
        self.password = password
        self.age = age
        self.sex = sex


class input2(db.Model):
    __tablename__ = 'User_20_2'
    height = db.Column(db.Float, primary_key=True)
    weight = db.Column(db.Float, nullable=True)
    waist = db.Column(db.Float, nullable=True)
    bloodpressure = db.Column(db.Integer, nullable=True)
    bodyfat = db.Column(db.Integer, nullable=True)


    def __init__(self, height, weight, waist, bloodpressure, bodyfat):
        self.height = height
        self.weight = weight
        self.waist = waist
        self.bloodpressure = bloodpressure
        self.bodyfat = bodyfat


class input3(db.Model):
    __tablename__ = 'User_20_3'
    flexibility = db.Column(db.Float, primary_key=True)
    muscle = db.Column(db.Float, nullable=True)
    alacrity = db.Column(db.Float, nullable=True)

    def __init__(self, flexibility, muscle, alacrity):
        self.flexibility = flexibility
        self.muscle = muscle
        self.alacrity = alacrity

class input_60_1(db.Model):
    __tablename__ = 'User_60_1'
    id = db.Column(db.String, primary_key=True)
    password = db.Column(db.Integer, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    sex = db.Column(db.Integer, nullable=True)

    def __init__(self, id, password, age, sex):
        self.id = id
        self.password = password
        self.age = age
        self.sex = sex


class input_60_2(db.Model):
    __tablename__ = 'User_60_2'
    height = db.Column(db.Float, primary_key=True)
    weight = db.Column(db.Float, nullable=True)
    waist = db.Column(db.Float, nullable=True)
    bloodpressure = db.Column(db.Integer, nullable=True)
    bodyfat = db.Column(db.Integer, nullable=True)

    def __init__(self, height, weight, waist, bloodpressure, bodyfat):
        self.height = height
        self.weight = weight
        self.waist = waist
        self.bloodpressure = bloodpressure
        self.bodyfat = bodyfat


class input_60_3(db.Model):
    __tablename__ = 'User_60_3'
    sit_band = db.Column(db.Float, primary_key=True)
    sit_up = db.Column(db.Float, nullable=True)
    sit_stand = db.Column(db.Float, nullable=True)
    return_3m = db.Column(db.Float, nullable=True)
    walk_8 = db.Column(db.Float, nullable=True)

    def __init__(self, sit_band, sit_up, sit_stand, return_3m, walk_8):
        self.sit_band = sit_band
        self.sit_up = sit_up
        self.sit_stand = sit_stand
        self.return_3m = return_3m
        self.walk_8 = walk_8


@app.route('/')
def re0():
    return render_template('index.html')



@app.route('/input_1', methods=['GET', 'POST'])
def re1():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        age = request.form['age']
        sex = request.form['sex']

        USER_20_1 = input1(name, password, age, sex)

        db.session.add(USER_20_1)
        db.session.commit()

        return redirect(url_for('re2'))
    return render_template('input_1.html')



@app.route('/input_2', methods=['GET', 'POST'])
def re2():
    if request.method == 'POST':
        height = request.form['height']
        weight = request.form['weight']
        waist = request.form['waist']
        bloodpressure = request.form['bloodpressure']
        bodyfat = request.form['bodyfat']

        USER_20_2 = input2(height, weight, waist, bloodpressure, bodyfat)

        db.session.add(USER_20_2)
        db.session.commit()

        return redirect(url_for('re3'))
    return render_template('input_2.html')



@app.route('/input_3', methods=['GET', 'POST'])
def re3():
    if request.method == 'POST':
        flexibility = request.form['flexibility']
        muscle = request.form['muscle']
        alacrity = request.form['alacrity']

        USER_20_3 = input3(flexibility, muscle, alacrity)

        db.session.add(USER_20_3)
        db.session.commit()

        return redirect(url_for('re4'))
    return render_template('input_3.html')


@app.route('/input_1_60', methods=['GET', 'POST'])
def re60_1():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        age = request.form['age']
        sex = request.form['sex']

        USER_1_60 = input_60_1(name, password, age, sex)

        db.session.add(USER_1_60)
        db.session.commit()

        return redirect(url_for('re60_2'))
    return render_template('input_1_60.html')


@app.route('/input_2_60', methods=['GET', 'POST'])
def re60_2():
    if request.method == 'POST':
        height = request.form['height']
        weight = request.form['weight']
        waist = request.form['waist']
        bloodpressure = request.form['bloodpressure']
        bodyfat = request.form['bodyfat']

        USER_2_60 = input_60_2(height, weight, waist, bloodpressure, bodyfat)

        db.session.add(USER_2_60)
        db.session.commit()

        return redirect(url_for('re60_3'))
    return render_template('input_2_60.html')



@app.route('/input_3_60', methods=['GET', 'POST'])
def re60_3():
    if request.method == 'POST':
        sit_band = request.form['sit_band']
        sit_up = request.form['sit_up']
        sit_stand = request.form['sit_stand']
        return_3m = request.form['return_3m']
        walk_8 = request.form['walk_8']

        USER_3_60 = input_60_3(sit_band, sit_up, sit_stand, return_3m, walk_8)

        db.session.add(USER_3_60)
        db.session.commit()

        return redirect(url_for('re7'))
    return render_template('input_3_60.html')



@app.route('/predict')
def re4():
    from read_sql import pre_result, main_result, last_result
    from youtube_crawling import find_link

    return render_template('predict.html', pre_result=pre_result, main_result=main_result, last_result=last_result, links=find_link())


@app.route('/predict_60')
def re7():
    from read_sql_60 import pre_result, main_result, last_result
    from youtube_crawling_60 import find_link

    return render_template('predict_60.html', pre_result=pre_result, main_result=main_result, last_result=last_result, links=find_link())


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

