from gendiff.parsing_files import parsing_files
from gendiff.stylish import stylish


def generate_diff(first_file, second_file):
    file1 = parsing_files(first_file)
    file2 = parsing_files(second_file)
    def walk(file1, file2, depth=1):
    
        res = {**file1, **file2}
        diff = []
        for k in sorted(res.keys()):
            if k in file2.keys() and k in file1.keys() and file1[k] == file2[k]:
                if type(file1[k]) is dict and type(file2[k]) is dict:
                    dictionary = {"status": "without changes, dict", "depth": depth, "key": k, "value": walk(file1[k], file2[k], depth + 1)}
                    diff.append(dictionary)
                else:
                
                    dictionary = {"status": "without changes", "depth": depth, "key": k,
                                 "value": file1[k]}
                    diff.append(dictionary)
            elif k in file2.keys() and k in file1.keys() and file1[k] != file2[k]:
                if type(file1[k]) is dict and type(file2[k]) is dict:
                    dictionary = {"status": "without changes, dict", "depth": depth,
                                 "key": k,
                                 "value": walk(file1[k], file2[k], depth + 1)}
                    diff.append(dictionary)
                elif type(file1[k]) is dict:
                    dictionary = {"status": "without changes, dict", "depth": depth,
                                 "key": k,
                                 "value": walk(file1[k], file1[k], depth + 1)}
                    diff.append(dictionary)
                elif type(file2[k]) is dict:
                    dictionary = {"status": "without changes, dict", "depth": depth,
                                 "key": k,
                                 "value": walk(file2[k], file2[k], depth + 1)}
                    diff.append(dictionary)
                else:
                    dictionary = {"status": "deleted", "depth": depth, "key": k,
                                 "value": file1[k]}
                    diff.append(dictionary)
                    dictionary = {"status": "added", "depth": depth, "key": k,
                                 "value": file2[k]}
                    diff.append(dictionary)
            elif k in file1:
                if type(file1[k]) is dict:
                    dictionary = {"status": "deleted, dict", "depth": depth,
                                 "key": k,
                                 "value": walk(file1[k], file1[k], depth + 1)}
                    diff.append(dictionary)
                else:
                   dictionary = {"status": "deleted", "depth": depth, "key": k,
                                "value": file1[k]}
                   diff.append(dictionary)
            elif k in file2:
                if type(file2[k]) is dict:
                    dictionary = {"status": "added, dict", "depth": depth,
                                 "key": k,
                                 "value": walk(file2[k], file2[k], depth + 1)}
                    diff.append(dictionary)
                else:
                    dictionary = {"status": "added", "depth": depth, "key": k,
                                 "value": file2[k]}
                    diff.append(dictionary)
        return stylish(diff)
    return walk(file1, file2)
