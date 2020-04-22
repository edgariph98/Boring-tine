# In the python console
import requests
import json
from pprint import pprint
url = 'https://wger.de/api/v2/exercise/search/term'
data = '{"key": "value"}'
headers = {'Accept': 'application/json',
         'Authorization':'28aafca4b20580c072fe3c87722eca33e13138ac'}
r = requests.patch(url=url, data=data, headers=headers)
pprint(json.loads(r.content))