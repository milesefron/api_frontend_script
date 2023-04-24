from __future__ import print_function
import urllib.request, json, urllib.parse , requests, sys

endpoint = "https://api.millercenter.org/speeches"

r = requests.post(url = endpoint)
data = r.json()
items = data['Items']

while 'LastEvaluatedKey' in data:
  parameters = {"continue_president": data['LastEvaluatedKey']['president'], 
                "continue_doc_name": data['LastEvaluatedKey']['doc_name']}
  r = requests.post(url = endpoint, params = parameters)
  data = r.json()
  items = items + data['Items']
  for item in data['Items']:
    print(item['title'], file=sys.stderr)

print(json.dumps(items))
