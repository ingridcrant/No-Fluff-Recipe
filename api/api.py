from flask import Flask, request
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

app = Flask(__name__)

@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    html = request.form['html']
    return "passed"