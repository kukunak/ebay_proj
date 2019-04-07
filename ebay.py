from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup
from flask import current_app
from config import EBAY_API_KEY


Keywords = input('введите интересующий товар\n')
api = finding(appid=EBAY_API_KEY, config_file=None)
api_request = { 'keywords': Keywords }
response = api.execute('findItemsByKeywords', api_request)
soup = BeautifulSoup(response.content,'lxml')

totalentries = int(soup.find('totalentries').text)
items = soup.find_all('item')

for item in items:
    cat = item.categoryname.string.lower()
    title = item.title.string.lower()
    price = int(round(float(item.currentprice.string)))
    url = item.viewitemurl.string.lower()

if __name__ == "__main__":
    print(item)


'''
    print('________')
    print('cat:\n' + cat + '\n')
    print('title:\n' + title + '\n')
    print('price:\n' + str(price) + '\n')
    print('url:\n' + url + '\n')
    input()
'''