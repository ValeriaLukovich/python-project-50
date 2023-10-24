import yaml
import json
from pathlib import Path


def find_suffix(file_to_find):
    extension = Path(file_to_find).suffix
    return extension


def parsing_files(file_to_parse):
    extension = find_suffix(file_to_parse)
    if extension == '.yml' or extension == '.yaml':
        with open(file_to_parse, "r") as read_file:
            dictionary = yaml.safe_load(read_file)
            return dictionary
    elif extension == '.json':
        with open(file_to_parse, "r") as read_file:
            dictionary = json.load(read_file)
            return dictionary
