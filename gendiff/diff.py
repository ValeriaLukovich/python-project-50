from gendiff.parsing_files import parsing_files
from gendiff.function_package.stylish import stylish
from gendiff.function_package.plain import plain
from gendiff.function_package.json import json_f


def make_dict(status, k, value, value1=0):
    dictionary = {
        "status": status,
        'key': k,
        'value': value,
        'value1': value1
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


def make_diff(first_file, second_file):
    file1 = parsing_files(first_file)
    file2 = parsing_files(second_file)

    def walk(file1, file2):
        union = {**file1, **file2}
        diff = []
        for k in sorted(union.keys()):
            child1 = file1.get(k)
            child2 = file2.get(k)
            if isinstance(child1, dict) and isinstance(child2, dict):
                res = make_dict("dict", k, walk(child1, child2))
                diff.append(res)
            else:
                diff.append(chek_key(k, file1, file2))
        return diff
    return walk(file1, file2)


def generate_diff(first_file, second_file, form="stylish"):
    lists = make_diff(first_file, second_file)
    if form == 'stylish':
        return stylish(lists)
    elif form == 'plain':
        return plain(lists)
    elif form == 'json':
        return json_f(lists)
