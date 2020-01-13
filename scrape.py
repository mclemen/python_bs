from bs4 import BeautifulSoup
import requests
import urllib.request
import lxml.html
# import csv
from pymongo import MongoClient
db_server = MongoClient('192.168.1.3', 27017) 
db = db_server.sportradar

sauce = urllib.request.urlopen('https://ls.sir.sportradar.com/future/en?fbclid=IwAR3W0CRBFmuDsY2D2ZiU-ARWb-uAV5TfOd5gwR6BkglkPxNM2NPqf0-xEEU').read()
soup = BeautifulSoup(sauce, 'lxml')

    # file = open('sportradar.csv', 'wt')
    # writer = csv.writer(file)

    # writer.writerow(('League', 'Teams', 'Total Score'))

table = soup.find('table')
table_rows = table.find_all('tr')

for tr in table_rows:
        tourn_info = tr.find_all('span', class_ = "visible-xs-inline")
        team_score = tr.find_all(string = "Score")
        td = tr.find_all('td', class_ = "teams", limit = 2)
        total_score = tr.find_all('td', class_ = "score", limit = 1)
        row = [i.text for i in td]
        league = [x.text for x in tourn_info]
        totalscore = [y.text for y in total_score]
        print(league + row + totalscore)
        #writer.writerow([league, row, totalscore])
        db.leagues.insert_one({'league':league, 'row':row, 'totalscore':totalscore})   

# file.close()