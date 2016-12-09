from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'https://en.wikipedia.org/wiki/Game_of_Thrones#Adaptation_schedule'
response = urlopen(url).read()
soup = BeautifulSoup(response)

for link in soup.findAll("a"):
    if link.string == "/wiki/Game_of_Thrones_(season_1)":
        season_url = 'https://en.wikipedia.org/wiki/Game_of_Thrones' + link["href"]
        season_html = urlopen(season_url).read()
        season_soup = BeautifulSoup(season_html)
        print season_soup.find("a href", attrs={"sea": "season"}).string