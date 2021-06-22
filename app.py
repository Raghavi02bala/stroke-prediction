from flask import Flask,render_template,url_for,request,jsonify
from flask_cors import cross_origin
import joblib

app = Flask(__name__)
with open('finalized_model.pkl' ,'rb') as f:
    loaded_model = joblib.load(f)
print("Model Loaded")

@app.route("/",methods=['GET'])
@cross_origin()
def home():
	return render_template("index.html")

@app.route("/predict",methods=['GET', 'POST'])
@cross_origin()
def predict():
	if request.method == "POST":
		gender = request.form['gender']
		age = request.form['age']
		hypertension = request.form['hypertension']
		heart_disease = request.form['heart_disease']
		residence = request.form['residence']
		avg_glucose_level = request.form['avg_glucose_level']
		bmi = request.form['bmi']
		smoking_status = request.form['smoking_status']
		ever_married = request.form['ever_married']
		work_type = request.form['work_type']

		input_lst = [gender,age,hypertension,heart_disease,ever_married,work_type,residence,avg_glucose_level,bmi,smoking_status]
		data = []
		
		data.append(input_lst[1])
		data.append(input_lst[2])
		data.append(input_lst[3])
		if input_lst[4] == 'Yes':
			data.append(1)
		else:
			data.append(0)
		data.append(input_lst[7])
		data.append(input_lst[8])
		if input_lst[0] == 'Male':
			data.append(0)
			data.append(1)
		if input_lst[0] == 'Female':
			data.append(1)
			data.append(0)
		if input_lst[5] == 'Private':
			data.append(0)
			data.append(0)
			data.append(1)
			data.append(0)
		if input_lst[5] == 'Self-employed':
			data.append(0)
			data.append(0)
			data.append(0)
			data.append(1)
		if input_lst[5] == 'Govt_job':
			data.append(1)
			data.append(0)
			data.append(0)
			data.append(0)
		if input_lst[5] == 'Never_worked':
			data.append(0)
			data.append(1)
			data.append(0)
			data.append(0) 
		if input_lst[6] == 'Urban':
			data.append(0)
			data.append(1)
		if input_lst[6] == 'Rural':
			data.append(1)
			data.append(0)
		if input_lst[9] == 'never smoked':
			data.append(0)
			data.append(0)
			data.append(1)
			data.append(0)    
		if input_lst[9] == 'Unknown':
			data.append(1)
			data.append(0)
			data.append(0)
			data.append(0)
		if input_lst[9] == 'formerly smoked':
			data.append(0)
			data.append(1)
			data.append(0)
			data.append(0)
		if input_lst[9] == 'smokes':
			data.append(0)
			data.append(0)
			data.append(0)
			data.append(1) 

		data = [data]
		pred = loaded_model.predict(data)
		if pred == 0:
			return render_template("negative.html")
		else:
			return render_template("positive.html")
	return render_template("predict.html")

if __name__=='__main__':
	app.run(debug=True)