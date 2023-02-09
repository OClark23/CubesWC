import main
import pytest


def first_test():
    data_entry = main.get_wufoo_data()
    for k, v in data_entry.item():
        assert len(data_entry) >= 10
