from flask import Flask, request, jsonify
import pickle
import json
import numpy as np

app = Flask(__name__)
model = pickle.load(open('random_forest_model.pkl', 'rb'))

@app.route('/')
def home():
    return 'Welcome to Stroke Prediction Solution API'

@app.route("/predict", methods = ["GET"])
def predict():
    age = request.args.get("age")
    gender = request.args.get("gender")
    hypertension = request.args.get("hypertension")
    heart_disease = request.args.get("heart_disease")
    ever_married = request.args.get("ever_married")
    work_type = request.args.get("work_type")
    Residence_type = request.args.get("Residence_type")
    avg_glucose_level = request.args.get("avg_glucose_level")
    bmi = request.args.get("bmi")
    smoking_status = request.args.get("smoking_status")

    makeprediction = model.predict([[age, gender, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status]])
    output = round(makeprediction[0],0)
    return jsonify({'Possibility of having a stroke is':output})
    
    print("0 means no stroke, 1 means stroke")
if __name__ =="__main__":
    app.run(debug=True)
