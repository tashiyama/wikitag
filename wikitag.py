from ensurepip import bootstrap
from flask import Flask
from flask import render_template, request, redirect, url_for
from flask import request
from flask_bootstrap import Bootstrap



app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')