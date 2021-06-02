from flask import Flask, request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    html = request.form['html']
    html_soup = BeautifulSoup(html, 'html.parser')
    image = html_soup.find('div', class_='inner-container js-inner-container image-overlay')
    ingredients = html_soup.find('div', class_='recipe-shopper-wrapper')
    instructions = html_soup.find('fieldset', class_='instructions-section__fieldset')

    content = str(image.img) + str(ingredients) + str(instructions)

    with open('recipe.html','w') as f:
        f.write(content)
    
    f.close()

    return 'Success', 200