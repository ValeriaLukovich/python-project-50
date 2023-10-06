from gendiff.parsing_files import parsing_files
from gendiff.stylish import stylish
from gendiff.make_dict import make_dict


def generate_diff(first_file, second_file, format=stylish):
    file1 = parsing_files(first_file)
    file2 = parsing_files(second_file)

    def walk(file1, file2, d=1):
        union = {**file1, **file2}
        diff = []
        for k in sorted(union.keys()):
            child1 = file1.get(k)
            child2 = file2.get(k)
            if not isinstance(child1, dict) and not isinstance(child2, dict):
                if k in file1 and k in file2 and file1[k] == file2[k]:
                    res = make_dict("without changes", d, k, file1[k])
                    diff.append(res)
                elif k in file1 and k in file2 and file1[k] != file2[k]:
                    res = make_dict("deleted", d, k, file1[k])
                    diff.append(res)
                    res = make_dict("added", d, k, file2[k])
                    diff.append(res)
                elif k in file1:
                    res = make_dict("deleted", d, k, file1[k])
                    diff.append(res)
                elif k in file2:
                    res = make_dict("added", d, k, file2[k])
                    diff.append(res)
            else:
                if type(child1) is dict and type(child2) is dict:
                    res = make_dict("dict", d, k, walk(child1, child2, d + 1))
                    diff.append(res)
                elif type(child1) is dict:
                    if k in file2:
                        res = make_dict("del dict", d, k, walk(child1, child1, d + 1))
                        diff.append(res)
                        res = make_dict("added", d, k, file2[k])
                        diff.append(res)
                    else:
                        res = make_dict("del dict", d, k, walk(child1, child1, d + 1))
                        diff.append(res)
                elif type(child2) is dict:
                    if k in file1:
                        res = make_dict("add dict", d, k, walk(child2, child2, d + 1))
                        diff.append(res)
                        res = make_dict("deleted", d, k, file1[k])
                        diff.append(res)
                    else:
                        res = make_dict("add dict", d, k, walk(child2, child2, d + 1))
                        diff.append(res)
        return diff
    return format(walk(file1, file2))
