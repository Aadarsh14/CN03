import requests
from bs4 import BeautifulSoup
import random

def scrapeWikiArticle(url):
	response = requests.get(
		url=url,
	)
	
	soup = BeautifulSoup(response.content, 'html.parser')

	title = soup.find(id="firstHeading")
	print(title.text)

	allLinks = soup.find(id="bodyContent").find_all("a")
	random.shuffle(allLinks)
	linkToScrape = 0

	for link in allLinks:
		# We are only interested in other wiki articles
		if link['href'].find("/wiki/") == -1: 
			continue

		# Use this link to scrape
		linkToScrape = link
		break

	scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])

scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")

def writeFile(data, searchQuery):
    
    with open('logs.txt', 'a') as fp:
        fp.write("\n"+searchQuery+"  "+data)
    showRes(data)


def progressBar():
    
    for i in tqdm (range (30), desc="Loading…", ascii=False, ncols=75):
        time.sleep(0.01)


def showRes(data):
    print("Below is your Search URL         All queries are logged into 'logs.txt'")
    print(data)
   
