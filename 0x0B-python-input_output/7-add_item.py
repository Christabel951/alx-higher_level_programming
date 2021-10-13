#!/usr/bin/python3
""" script that adds all args to a Py list, then save them to a file """
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    py_list = load_from_json_file(filename)
except:
    py_list = []
finally:
    for i in sys.argv[1:]:
        py_list.append(i)
    save_to_json_file(py_list, filename)
