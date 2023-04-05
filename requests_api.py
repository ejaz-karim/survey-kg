import requests
import rdflib



endpoint_url = "https://api.dbpedia-spotlight.org/en/annotate"

with open("seeAlso.txt", "r", encoding="utf-8") as f:
    text = f.read()

params = {
    "text": text,
    "confidence": 0.6,
    "support": 20,
}

# Send request to API and print response
headers = {'Accept': 'text/html'}

response = requests.get(endpoint_url, params=params, headers=headers)

print(response)

if response.status_code == 200:
    annotations = response.text
    with open("requests_output.txt", "w", encoding="utf-8") as g:
        g.write(annotations)
else:
    print("Error:", response.status_code)