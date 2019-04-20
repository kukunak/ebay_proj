from config import EBAY_API_KEY
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

try:
    api = Finding(appid=EBAY_API_KEY, config_file=None)
    response = api.execute('findItemsAdvanced', {'keywords': 'iphone'})
    dictr = response.dict()
    print(dictr)
  
except ConnectionError as e:
    print(e)
    print(e.response.dict())