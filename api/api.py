from flask import Flask, request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    html = request.form['html']
    html_soup = BeautifulSoup(html, 'html.parser')
    title = html_soup.find('div', class_='intro article-info')
    image = html_soup.find('div', class_='inner-container js-inner-container image-overlay')
    originalservingamt = html_soup.find('div', class_='recipe-adjust-servings__size-quantity')
    ingredients = html_soup.find('ul', class_='ingredients-section')
    instructions = html_soup.find('ul', class_='instructions-section')

    originalservingamt = originalservingamt.text
    ingredientsheader = '<h2>Ingredients</h2>'
    instructionsheader = '<h2>Instructions</h2>'
    header = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8" />\n<link rel="stylesheet" href="recipestyle.css" />\n<script src="scripts.js"></script>\n<title>Recipe</title>\n</head>\n'
    plusminusbutton = '<div class="number">\n<span class="minus">-</span>\n<input class="inputsized" type="text" value="'+originalservingamt+'"/>\n<span class="plus">+</span>\n</div>\n'

    stepcount = 0

    instructiontext = '<ul>'

    for item in instructions.findAll('li'):
        stepcount += 1
        instructiontext += '<h3>Step '+str(stepcount)+'</h3>\n'
        instructiontext += str(item.div)+"\n"
    
    instructiontext += '</ul>\n'

    content = str(title) + str(image.img) + plusminusbutton + ingredientsheader + str(ingredients) + instructionsheader + instructiontext

    with open('recipe.html','w') as f:
        f.write(header)
        f.write('<body>\n')
        f.write('<div class="container">\n')
        f.write(content)
        f.write('<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js"></script>\n')
        f.write('<script src="scripts.js" type="text/javascript"></script>\n')
        f.write('</div>\n')
        f.write('</body>\n')
        f.write('</html>')
    
    f.close()

    return 'Success', 200