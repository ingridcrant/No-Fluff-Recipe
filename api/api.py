from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    html = request.form['html']
    html_soup = BeautifulSoup(html, 'html.parser')
    
    recipetemplates = [html_soup.find('div', class_=re.compile('^wprm-recipe-container')),
                    html_soup.find('div', id=re.compile('^wpurp-container-recipe-')),
                    html_soup.find('div', id=re.compile('^tasty-recipes')),
                    html_soup.find('div', id=re.compile('^post-recipe')),
                    html_soup.find('div', id=re.compile('^structured-project-content')),
                    html_soup.find('div', id="recipe"),
                    html_soup.find('div', itemtype="http://schema.org/Recipe")]
    
    content = '<div class="container">'

    for recipetemplate in recipetemplates:
        if recipetemplate:
            content += str(recipetemplate)
            break

    content += "</div>"
    
    response = jsonify(recipe=content)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response