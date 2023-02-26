##########################################################################
## Imports
##########################################################################

from do_prediction import predict

import os

from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask.json import jsonify


##########################################################################
## Application Setup
##########################################################################

app = Flask(__name__)


##########################################################################
## Routes
##########################################################################

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/classify/<row_of_pixel>")
def classification_result(row_of_pixel):
    """
    Accepts a row of pixels (same format of data in the training dataset) and returns the classification result.
    """
    prediction = predict(eval(row_of_pixel))
    return jsonify({"classification result": f'{prediction}'})


##########################################################################
## Main
##########################################################################

if __name__ == '__main__':
    app.run()