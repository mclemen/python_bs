from bs4 import BeautifulSoup
import requests
import urllib.request
import lxml.html

#from pymongo import MongoClient 
#db_server = MongoClient('192.168.1.6', 27017) # Connect to the MongoDB server
#db = db_server.sportradar # Database name = sportradar

sauce = urllib.request.urlopen('https://ls.sir.sportradar.com/future/en?fbclid=IwAR3W0CRBFmuDsY2D2ZiU-ARWb-uAV5TfOd5gwR6BkglkPxNM2NPqf0-xEEU').read()
soup = BeautifulSoup(sauce, 'lxml')

table = soup.find('table')
table_rows = table.find_all('tr')

for tr in table_rows:
    tourn_info = tr.find_all('span', class_ = "visible-sm-inline") # Scrape the Countries
    td = tr.find_all('td', class_ = "teams") # Scrape the Teams
    total_score = tr.find_all('td', class_ = "score", limit = 1) # Scrape their Scores
    team = [i.text.strip() for i in td]
    league = [x.text.strip() for x in tourn_info]
    totalscore = [y.text.strip() for y in total_score]

    if league == []:
        print('')
    else:
        print(league)
        db.leagues.insert_one({'league':league})  #insert data to the MongoDB collection 

    if team == []:
        print('')
    else:
        print(team, totalscore)
        db.leagues.insert_one({'team':team, 'totalscore': totalscore})




