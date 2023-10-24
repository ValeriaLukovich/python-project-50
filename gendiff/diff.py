from gendiff.parsing_files import parsing_files
from gendiff.function_package.stylish import make_stylish
from gendiff.function_package.plain import make_plain
from gendiff.function_package.json import make_json


def make_dict(status, k, value, new_value=None):
    dictionary = {
        "status": status,
        'key': k,
        'value': value,
        'new_value': new_value
    }
    return dictionary


def chek_key(k, file1, file2):
    if k in file1 and k in file2 and file1[k] == file2[k]:
        res = make_dict("without changes", k, file1[k])
    elif k in file1 and k in file2 and file1[k] != file2[k]:
        res = make_dict("updated", k, file1[k], file2[k])
    elif k in file1:
        res = make_dict("deleted", k, file1[k])
    elif k in file2:
        res = make_dict("added", k, file2[k])
    return res


def make_diff(file1, file2):
    union = {**file1, **file2}
    diff = []
    for k in sorted(union.keys()):
        child1 = file1.get(k)
        child2 = file2.get(k)
        if isinstance(child1, dict) and isinstance(child2, dict):
            res = make_dict("dict", k, make_diff(child1, child2))
            diff.append(res)
        else:
            diff.append(chek_key(k, file1, file2))
    return diff


def generate_diff(first_file, second_file, form="stylish"):
    file1 = parsing_files(first_file)
    file2 = parsing_files(second_file)
    lists = make_diff(file1, file2)
    if form == 'stylish' or not form:
        return make_stylish(lists)
    elif form == 'plain':
        return make_plain(lists)
    elif form == 'json':
        return make_json(lists)
    else:
        raise ValueError("Input correct argument")
