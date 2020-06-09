import requests

r = requests.get('http://covidtracking.com/api/v1/states/current.json')
data = r.json()
for d in data:
  new_positives = d["positiveIncrease"]
  new_tests = d["totalTestResultsIncrease"]
  if(new_tests == 0):
    d["pct_positive"] = 0
  else:
    d["pct_positive"] = new_positives/new_tests
results = sorted(data, key=lambda x: x["pct_positive"])
for i, state in enumerate(results):
  print(f'{i+1} - {state["state"]}: {state["pct_positive"]}')
