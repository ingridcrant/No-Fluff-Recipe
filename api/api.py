from flask import Flask, request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    html = request.form['html']
    html_soup = BeautifulSoup(html, 'html.parser')

    content = ''
    for EachPart in html_soup.select('div[class*="wprm-recipe-template"]'):
        content += str(EachPart)

    return content