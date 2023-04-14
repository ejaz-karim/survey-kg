import requests_api
import filter_requests_output

with open("seeAlso.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

tuple = tuple(line.strip() for line in lines)

with open("survey7.ttl", "r", encoding="utf-8") as g:
    seeAlso_count = 0
    for word in tuple:
        requests_api.db_api(word)
        filter_requests_output.iteration()
        

