from flask import Flask, request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    html = request.form['html']
    html_soup = BeautifulSoup(html, 'html.parser')
    title = html_soup.find('div', class_='intro article-info')
    image = html_soup.find('div', class_='inner-container js-inner-container image-overlay')
    originalservingamt = html_soup.find('div', class_='recipe-adjust-servings__original-serving')
    ingredients = html_soup.find('ul', class_='ingredients-section')
    instructions = html_soup.find('ul', class_='instructions-section')

    originalserving = '<h3>'+originalservingamt.text+'</h3>'
    ingredientsheader = '<h2>Ingredients</h2>'
    instructionsheader = '<h2>Instructions</h2>'
    header = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8" /><link rel="stylesheet" href="recipestyle.css" /><title>Recipe</title></head>'
    
    content = header + str(title) + str(image.img) + originalserving + ingredientsheader + str(ingredients) + instructionsheader + str(instructions)

    with open('recipe.html','w') as f:
        f.write('<div class="container">')
        f.write(content)
        f.write('</div>')
    
    f.close()

    return 'Success', 200