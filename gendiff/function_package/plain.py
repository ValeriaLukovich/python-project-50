from gendiff.generate_diff import generate_diff


def new_format(string):
    res = string.replace("'False'", "false")
    return res.replace("'True'", "true").replace("'None'", "null")


def plain(lists, path='', res=[]):
    for elem in lists:
        if elem['status'] == "dict":
            plain(elem['value'], path + elem['key'] + '.')
        else:
            if elem['status'] == "deleted":
                res.append(f"Property '{path}{elem['key']}' was removed")
            elif elem['status'] == "added":
                if isinstance(elem['value'], dict):
                    res.append(f"Property '{path}{elem['key']}' was added with value: [complex value]")
                else:
                    res.append(f"Property '{path}{elem['key']}' was added with value: '{str(elem['value'])}'")
            elif elem['status'] == "updated":
                if isinstance(elem['value1'], dict):
                    res.append(f"Property '{path}{elem['key']}' was updated. From [complex value] to '{str(elem['value2'])}'")
                elif isinstance(elem['value2'], dict):
                    res.append(f"Property '{path}{elem['key']}' was updated. From '{str(elem['value1'])}' to [complex value]")
                else:
                    res.append(f"Property '{path}{elem['key']}' was updated. From '{str(elem['value1'])}' to '{str(elem['value2'])}'")
    return new_format("\n".join(res))
