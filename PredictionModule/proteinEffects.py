#Get a json which contains all efects for a specific protein name
# proteinName is the name of the protein and limit is the limit of effects that will be in JSON
#you should use python 3 to run this

import requests, sys, json

proteinName = "dof zinc fingers"
limit = 5


proteinName = proteinName.replace(' ', '%20')

requestURL = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=" + str(proteinName) + "&limit=" + str(limit) + "&" + "page=1";

print(requestURL)

r = requests.get(requestURL, headers={ "Accept" : "application/json"})

if not r.ok:
  r.raise_for_status()
  sys.exit()

responseBody = r.text
parsed = json.loads(responseBody)

print(json.dumps(parsed, indent=2, sort_keys=True))
