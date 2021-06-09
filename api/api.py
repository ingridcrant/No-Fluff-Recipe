from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    html = request.form['html']
    html_soup = BeautifulSoup(html, 'html.parser')
    
    content = ""
    for EachPart in html_soup.select('div[class*="wprm-recipe-container"]'):
        content += str(EachPart)
    
    response = jsonify(recipe=content)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response