import sys

import requests
from requests.auth import HTTPBasicAuth

from Database import open_db
from secrets import wufoo_key

# from Database import open_db, close_db, create_entries_tables, setup_db


# adjust this to your URL
url = "https://oclark.wufoo.com/api/v3/forms/cubes-project/entries.json"


def get_wufoo_data() -> dict:
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    jsonresponse = response.json()
    return jsonresponse


def main():
    data = get_wufoo_data()
    data1 = data['Entries']
    file_to_save = open("output.txt", 'w')
    save_data(data1, save_file=file_to_save)

    _, cursor = open_db("Entries.db")
    #create_entries_tables(cursor)
    #close_db(connection)
    #setup_db()


def save_data(data_to_save: list, save_file=None):
    for entry in data_to_save:
        for key, value in entry.items():
            print(f"{key}: {value}", file=save_file)
        # now print the spacer
        print("+++++++++++++++++++++++++++++++++++++++++++++\n_______________________________________________",
              file=save_file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
