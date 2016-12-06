from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

def main():

    url = 'https://en.wikipedia.org/wiki/Game_of_Thrones'
    response = urlopen(url).read()
    soup = BeautifulSoup(response)

    total = 0

    seasonCounter = 7
    for link in soup.findAll("a"):
        if seasonCounter > 0:
            if isinstance(link.string, basestring):
                if link.string[:7] == "Season ":
                    seasonCounter -= 1
                    season_url = 'https://en.wikipedia.org' + link["href"]
                    print season_url
                    season_html = urlopen(season_url).read()
                    season_soup = BeautifulSoup(season_html)

                    allTableData = season_soup.findAll("td", attrs={"class": "description"})
                    for item in allTableData:
                        numberString = str(item.findPrevious("td"))[4:8]
                        number = float(numberString)
                        total += number

    print "Game of Thrones has seen a total of " + str(total) + " million US viewers on the original air dates of all of its episodes combined."


if __name__ == "__main__":
    main()