import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

# scraping student housing
url = "https://listings.och.uwaterloo.ca/Listings/Search/Results"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('tbody')
appts = table.find_all('tr')
imgs = []

# extracts images of each apartment
# stores them in the 2d list, imgs
for appt in appts:
    td = appt.find('td')
    atags = td.find_all('a')
    apptimgs = []

    for atag in atags:
        hreftag = atag['href']
        if '/Pictures' in hreftag:
            apptimgs.append('https://listings.och.uwaterloo.ca'+hreftag)

    imgs.append(apptimgs)

print(imgs)