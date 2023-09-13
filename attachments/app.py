from flask import Flask,request
app = Flask(__name__)

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC # "Support Vector Classifier"
def reg(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    nx = [inps]
    pred = linear_regressor.predict(nx)
    return pred

def classify(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    Y=Y.round()
    clf = SVC(kernel='linear') 
    clf.fit(X,Y)
    nx = [inps]
    pred = clf.predict(nx)
    return pred
@app.route('/', methods=['GET', 'POST'])
def index():
    eye_blink_rate = int(request.form.get('eye_blink_rate'))
    yawning_rate = int(request.form.get('yawning_rate'))
    lane_departure_without_signal = int(request.form.get('lane_departure_without_signal'))
    head_nodding_off = int(request.form.get('head_nodding_off'))
    sudden_stearing_movement = int(request.form.get('sudden_stearing_movement'))
    drugs = int(request.form.get('drugs'))
    medication = int(request.form.get('medication'))
    sleep_duration = int(request.form.get('sleep_duration'))
    tiredness = float(request.form.get('tiredness'))
    p = reg('driver drowsiness.csv',["eye_blink_rate","yawning_rate","lane_departure_without_signal","head_nodding_off","sudden_stearing_movement","drugs","medication","sleep_duration","tiredness"],"outcome",[eye_blink_rate,yawning_rate,lane_departure_without_signal,head_nodding_off,sudden_stearing_movement,drugs,medication,sleep_duration,tiredness])
    print("Bot : The outcome is: ",float(p[0]))
    p = classify('driver drowsiness.csv',["eye_blink_rate","yawning_rate","lane_departure_without_signal","head_nodding_off","sudden_stearing_movement","drugs","medication","sleep_duration","tiredness"],"class",[eye_blink_rate,yawning_rate,lane_departure_without_signal,head_nodding_off,sudden_stearing_movement,drugs,medication,sleep_duration,tiredness])
    if int(p[0]) == 0:
        print("DRIVER IS NOT SLEEPY!")
        pr = "DRIVER IS NOT SLEEPY!"
    elif int(p[0]) == 1:
        print("DRIVER IS SLEEPY!")
        pr = "DRIVER IS SLEEPY!"
    return pr

if __name__ == '__main__':
    app.run(debug=True)