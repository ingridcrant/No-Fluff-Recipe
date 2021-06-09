from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    html = request.form['html']
    html_soup = BeautifulSoup(html, 'html.parser')
    
    content = '<div class="container">'
    for EachPart in html_soup.select('div[class*="wprm-recipe-container"]'):
        content += str(EachPart)
    
    if html_soup.find('div', id=re.compile('^wpurp-container-recipe-')):
        content += str(html_soup.find('div', id=re.compile('^wpurp-container-recipe-')))
    
    if html_soup.find('div', id=re.compile('^tasty-recipes')):
        content += str(html_soup.find('div', id=re.compile('^tasty-recipes')))
    
    if html_soup.find('div', id=re.compile('^post-recipe')):
        content += str(html_soup.find('div', id=re.compile('^post-recipe')))
    
    if html_soup.find('div', id=re.compile('^structured-project-content')):
        content += str(html_soup.find('div', id=re.compile('^structured-project-content')))

    if html_soup.find('div', itemtype="http://schema.org/Recipe"):
        content += str(html_soup.find('div', itemtype="http://schema.org/Recipe"))
    
    if html_soup.find('div', itemtype="https://schema.org/Recipe"):
        content += str(html_soup.find('div', itemtype="https://schema.org/Recipe"))
    
    content += "</div>"
    
    response = jsonify(recipe=content)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response