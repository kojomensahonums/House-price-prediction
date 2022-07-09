import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__) # flask object
model= pickle.load(open('modell.pickle', 'rb'))

@app.route('/')# method
def home():
    return render_template('index.html')

@app.route('/predict', methods= ['POST'])# method
def predict():
    ''' For rendering results on HTML GUI'''
    int_features= [int(x) for x in request.form.values()]
    final_features= [np.array(int_features)]
    prediction= model.predict(final_features)
    
    output= np.round(prediction[0]*100000, 2)
    
    return render_template('index.html', prediction_text= 'House price should be $ {}'.format(output))

if __name__ == '__main__':
    app.run(debug= False)