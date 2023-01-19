import pickle
import os
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy 
import pandas
import matplotlib

app=Flask(__name__)
#load the model
regmodel = model = pickle.load(open('regmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
