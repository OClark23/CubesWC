import json
import sys
import requests
import response as response
from eventlet.green import urllib2
from requests.auth import HTTPBasicAuth

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from secrets import wufoo_key

base_url = 'https://oclark.wufoo.com/api/v3/'
username = wufoo_key
password = 'NewPassword'

file1    = open('entries_file.txt', 'w')
file1 = open('entries_file.txt', 'a')

def get_forms():
    response = requests.get(base_url+ "forms/cubes-project-proposal-", "submission.json")
        auth = (username, password))
    data1 = json.loads(response.text)
    print(json.dumps(data1, indent=4, sort_keys=true))
def get_wufoo_data() -> dict:
    url = "https://oclark.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries.json"
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
    sys.exit(-1)
    jsonresponse = response.json()
    return jsonresponse  # json response will be either a dictionary or a list of dictionaries

def get_fields():
    data = json.loads(response.text)
    wufooxtxt.write(str(data))


response = requests.get(base_url + 'cubes-project.json/entries')


# each dictionary represents a json object
def get_wufooform():
    response = requests.get(base_url + 'cubes-project.json')


if __name__ == '__main__':
    get_wufoo_data()
