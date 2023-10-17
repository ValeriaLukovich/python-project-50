import yaml
import json
from yaml.loader import SafeLoader


def parsing_files(file_to_parse):
    if file_to_parse.endswith('.yml') or file_to_parse.endswith('.yaml'):
        return yaml.load(open(file_to_parse), Loader=SafeLoader)
    elif file_to_parse.endswith('.json'):
        return json.load(open(file_to_parse))
