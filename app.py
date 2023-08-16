from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer
from PIL import Image 
import io
from predict import predict
# Define a flask app
app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        
        img = Image.open(io.BytesIO(f.read()))
        img = img.convert("RGB")
        label = predict(img)

        return str(label)
    return redirect(url_for('index'))  #None


if __name__ == '__main__':
    app.run(debug=True)
