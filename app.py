# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('rf_predictor_bp.pkl','rb'))

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])

def predict():
     if request.method == 'POST':
            
        level_hg = float(request.form['Level_of_Hemoglobin'])
        gpc = float(request.form['Genetic_Pedigree_Coefficient'])
        age = int(request.form['Age'])
        bmi = float(request.form['BMI'])
        sex = float(request.form['Sex'])
        pa = int(request.form['Physical_activity'])
        acpd = int(request.form['alcohol_consumption_per_day'])
        ckd = int(request.form['Chronic_kidney_disease'])
        atd = int(request.form['Adrenal_and_thyroid_disorders'])
        salt_diet =float(request.form['salt_content_in_the_diet'])
        
        
        data = np.array([[level_hg, gpc,age,bmi,sex,pa,acpd,ckd,atd,salt_diet]])
        my_prediction = model.predict(data)
        
        return render_template('result.html', prediction=my_prediction)
        
            

if  __name__ == '__main__':
    app.run(debug = True)