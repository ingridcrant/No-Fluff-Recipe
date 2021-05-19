from bs4 import BeautifulSoup
from urllib.request import urlopen

# scraping student housing
url = "https://listings.och.uwaterloo.ca/Listings/Search/Results"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

prices = soup.find_all("td", {"class": "t-last"})

print(prices)