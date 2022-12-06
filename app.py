from flask import Flask, render_template, url_for, request, jsonify
import pickle
import numpy as np

#create flask app
app =  Flask(__name__)

#load the pickle model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html', **locals())

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]  #à modifier pour pouvoir mettre du texte
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    #output = round(prediction[0],2)

    return render_template('index.html', prediction_text='The predicted number of rented bikes is {}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)

