from gendiff.parsing_files import parsing_files
from gendiff.stylish import stylish


def generate_diff(first_file, second_file, format=stylish):
    file1 = parsing_files(first_file)
    file2 = parsing_files(second_file)
    
    def walk(file1, file2, depth=1):
        res = {**file1, **file2}
        diff = []
        for k in sorted(res.keys()):
            children1 = file1.get(k)
            children2 = file2.get(k)
            if not isinstance(children1, dict) and not isinstance(children2, dict):
                if k in file1 and k in file2 and file1[k] == file2[k]:
                    dictionary = {"status": "without changes", "depth": depth, "key": k, "value": file1[k]}
                    diff.append(dictionary)
                elif k in file1 and k in file2 and file1[k] != file2[k]:
                    dictionary = {"status": "deleted", "depth": depth, "key": k, "value": file1[k]}
                    diff.append(dictionary)
                    dictionary = {"status": "added", "depth": depth, "key": k, "value": file2[k]}
                    diff.append(dictionary)
                elif k in file1:
                    dictionary = {"status": "deleted", "depth": depth, "key": k, "value": file1[k]}
                    diff.append(dictionary)
                elif k in file2:
                    dictionary = {"status": "added", "depth": depth, "key": k, "value": file2[k]}
                    diff.append(dictionary)
            else:
                if type(children1) is dict and type(children2) is dict:
                    dictionary = {"status": "dict", "depth": depth, "key": k, "value": walk(children1, children2, depth + 1)}
                    diff.append(dictionary)
                elif type(children1) is dict:
                    if k in file2:
                        dictionary = {"status": "deleted dict", "depth": depth, "key": k, "value": walk(children1, children1, depth + 1)}
                        diff.append(dictionary)
                        dictionary = dictionary = {"status": "added", "depth": depth, "key": k, "value": file2[k]}
                        diff.append(dictionary)
                    else:
                        dictionary = {"status": "deleted dict", "depth": depth, "key": k, "value": walk(children1, children1, depth + 1)}
                        diff.append(dictionary)
                elif type(children2) is dict:
                    if k in file1:
                        dictionary = {"status": "added dict", "depth": depth, "key": k, "value": walk(children2, children2, depth + 1)}
                        diff.append(dictionary)
                        dictionary = {"status": "deleted", "depth": depth, "key": k, "value": file1[k]}
                        diff.append(dictionary)
                    else:
                        dictionary = {"status": "added dict", "depth": depth, "key": k, "value": walk(children2, children2, depth + 1)}
                    diff.append(dictionary)
        return diff
    return format(walk(file1, file2))
