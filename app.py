import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('finalized_model.sav', 'rb'))
vec = pickle.load(open('vec.sav', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    #int_features = [str(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    output = ''

    if len(str(request.form.values())) > 1:

        prediction = model.predict(vec.transform(pd.Series(request.form.values())))

        if prediction[0] == 4:
            output = 'positive'
        if prediction[0] == 0:
            output = 'negative'

        return render_template('index.html', prediction_text='Your sentence is {}'.format(output))
    
    else:

        return render_template('index.html', prediction_text='Please enter a valid sentence')

#@app.route('/predict_api',methods=['POST'])
#def predict_api():
    '''
    For direct API calls trought request
    '''
#    data = request.get_json(force=True)
#    prediction = model.predict([np.array(list(data.values()))])

#    output = prediction[0]
#    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)