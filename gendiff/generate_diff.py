from gendiff.parsing_files import parsing_files
from gendiff.function_package import stylish


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
                res = {"status": "dict", 'depth': d, 'key': k, 'value': walk(child1, child2, d + 1)}
                diff.append(res)
            else:
                if k in file1 and k in file2 and file1[k] == file2[k]:
                    res = {"status": "without changes", 'depth': d, 'key': k, 'value': file1[k]}
                    diff.append(res)
                elif k in file1 and k in file2 and file1[k] != file2[k]:
                    res = {"status": "updated", 'depth': d, 'key': k, 'value1': file1[k], 'value2': file2[k]}
                    diff.append(res)
                elif k in file1:
                    res = {"status": "deleted", 'depth': d, 'key': k, 'value': file1[k]}
                    diff.append(res)
                elif k in file2:
                    res = {"status": "added", 'depth': d, 'key': k, 'value': file2[k]}
                    diff.append(res)
        return diff
    return format(walk(file1, file2))
