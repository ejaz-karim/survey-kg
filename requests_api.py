import requests

endpoint_url = "https://api.dbpedia-spotlight.org/en/annotate"

def db_api(text):

    params = {
        "text": text,
        "confidence": 0.5,
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
        return None