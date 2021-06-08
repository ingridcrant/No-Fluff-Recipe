from flask import Flask, request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    html = request.form['html']
    html_soup = BeautifulSoup(html, 'html.parser')

    header = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8" />\n<link rel="stylesheet" href="recipestyle.css" />\n<title>Recipe</title>\n</head>\n'
    
    content = ''
    for EachPart in html_soup.select('div[class*="wpurp-container"]'):
        content += str(EachPart)
    
    return content