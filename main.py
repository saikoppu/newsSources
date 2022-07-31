from urllib.request import urlopen
from bs4 import BeautifulSoup
link = urlopen("https://www.bbc.com/")
soup = BeautifulSoup(link)
a = soup.findAll("a", attrs = {"class": "block-link__overlay-link"})
headlines = {}
counter = 0
for headline in a:
  counter = counter + 1
  headlinename = headline.getText().strip()
  headlinelink = headline["href"]
  print(counter, ". ", headlinename, ": ", headlinelink)
