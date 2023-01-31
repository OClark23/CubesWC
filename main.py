import sys
import requests
from requests.auth import HTTPBasicAuth

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from secrets import wufoo_key

base_url = 'https://oclark.wufoo.com/api/v3/'
username = 'UserName !'
password = 'NewPassword'


wufooxtxt = open('wuffo.txt')
wufootxt2 = open ('wuffo.txt')



def get_wufoo_data() -> dict:
    url = "https://oclark.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries.json"
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
    sys.exit(-1)
    jsonresponse = response.json()
    return jsonresponse  # json response will be either a dictionary or a list of dictionaries

def test_wufoo_dict(get_data)
data = get_data
# each dictionary represents a json object

def get_wuffo_data(get_data)
data = get_data
if __name__ == '__main__':
    get_wufoo_data()
