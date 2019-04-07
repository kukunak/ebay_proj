# https://github.com/timotheus/ebaysdk-python/wiki/Finding-API-Class
# Sandbox Usage

from ebaysdk.finding import Connection as Finding

api = Finding(domain='svcs.sandbox.ebay.com', appid="YOUR_APPID", config_file=None)
response = api.execute('findItemsAdvanced', {'keywords': 'Python'})
print(response.dict())

# DT my addon
content_dict = response.dict()
len(content_dict['searchResult'])
# 2
len(content_dict['searchResult']['item'])
# 100

import json
with open("find_python.json", "w") as f:
    f.write(json.dumps(response.dict())
