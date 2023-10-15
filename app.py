from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__)  # initializing a flask app

@app.route('/', methods=['GET']) # route ti display the home page
def homepage():
    return render_template('index.html')

@app.route('/train', methods=['GET']) # route to train the pipeline
def training():
    os.system('python main.py')
    return 'Training Successful!'

@app.route('/predict', methods=['POST', 'GET']) # route to show the prediction in a web UI
def index():
    if request.method == 'POST':
        try:
            # reading the inputs given by the user
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 8080, debug=True)



