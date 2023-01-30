import sys

import HTTPBasicAuth
import requests
from requests.auth import HTTPBasicAuth

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from secrets import wufoo_key


def get_wufoo_data() -> dict:
    url = "https://jsantore.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries/json"
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
    sys.exit(-1)
    jsonresponse = response.json()
    return jsonresponse  # json response will be either a dictionary or a list of dictionaries


# each dictionary represents a json object

if __name__ == '__main__':
    get_wufoo_data()
