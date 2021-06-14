from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
import re

def clone(soup, tag):
    newtag = soup.new_tag(tag.name)
    for attr in tag.attrs:
        newtag[attr] = tag[attr]
    return newtag

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
                    html_soup.find('div', itemtype="http://schema.org/Recipe"),
                    html_soup.find('div', itemtype="https://schema.org/Recipe"),
                    html_soup.find('section', class_=re.compile('^mv-create-card'))]
    
    currenttags = "Not a compatible site"

    for recipetemplate in recipetemplates:
        if recipetemplate:
            currenttags = str(recipetemplate)
            fronttag = True

            for parent in recipetemplate.find_parents():
                parenttags = str(clone(html_soup, parent)).split("><")
                parentfronttag = parenttags[0] + ">"
                parentbacktag = "<" + parenttags[1]

                currenttags = parentfronttag + currenttags + parentbacktag

                if "body" in parentbacktag:
                    break
            
            break
    
    response = jsonify(recipe=currenttags)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response