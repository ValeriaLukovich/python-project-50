from gendiff.parsing_files import parsing_files
from gendiff.function_package.stylish import stylish


def make_dict(status, d, k, value, value1=0):
    dictionary = {
        "status": status,
        'depth': d,
        'key': k,
        'value': value,
        'value1': value1
        }
    return dictionary


def generate_diff(first_file, second_file, format=stylish):
    file1 = parsing_files(first_file)
    file2 = parsing_files(second_file)

    def walk(file1, file2, d=1):
        union = {**file1, **file2}
        diff = []
        for k in sorted(union.keys()):
            child1 = file1.get(k)
            child2 = file2.get(k)
            if isinstance(child1, dict) and isinstance(child2, dict):
                res = make_dict("dict", d, k, walk(child1, child2, d + 1))
                diff.append(res)
            else:
                if k in file1 and k in file2 and file1[k] == file2[k]:
                    res = make_dict("without changes", d, k, file1[k])
                    diff.append(res)
                elif k in file1 and k in file2 and file1[k] != file2[k]:
                    res = make_dict("updated", d, k, file1[k], file2[k])
                    diff.append(res)
                elif k in file1:
                    res = make_dict("deleted", d, k, file1[k])
                    diff.append(res)
                elif k in file2:
                    res = make_dict("added", d, k, file2[k])
                    diff.append(res)
        return diff
    return format(walk(file1, file2))
