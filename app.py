from flask import Flask,redirect,request,render_template,url_for
import pickle
import numpy as np

app = Flask(__name__)
app.use_static_for = 'static'


pickled_model = pickle.load(open('trend.pkl',"rb"))

@app.route('/')
def Index():
    return render_template("index1.html")
@app.route('/predict',methods= ['POST','GET'])
def predict():
    prediction = request.args.get('prediction')
    return render_template("result1.html",prediction= prediction)
@app.route('/result1.html',methods = ['POST','GET'])
def model1():
    if request.method == 'POST':
        precipitation = float(request.form['precipitate'])
        temp_max = float(request.form['temp_max'])
        temp_min = float(request.form['temp_min'])
        wind = float(request.form['wind'])

        weather = pickled_model.predict([[precipitation,temp_max,temp_min,wind]])
       
        return redirect(url_for('predict',prediction = weather))
    return render_template('result1.html')
if __name__ == '__main__':
    app.run(debug=True)