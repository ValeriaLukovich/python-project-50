def new_format(string):
    res = string.replace("'False'", "false")
    return res.replace("'True'", "true").replace("'None'", "null")


def plain(lists, path='', res=[]):
    for elem in lists:
        k = elem['key']
        v = elem['value']
        v1 = elem['value1']
        if elem['status'] == "dict":
            plain(v, path + elem['key'] + '.')
        else:
            if elem['status'] == "deleted":
                res.append(f"Property '{path}{k}' was removed")
            elif elem['status'] == "added":
                if isinstance(v, dict):
                    res.append(f"Property '{path}{k}' "
                               f"was added with value: [complex value]")
                else:
                    res.append(f"Property '{path}{k}' "
                               f"was added with value: '{str(v)}'")
            elif elem['status'] == "updated":
                if isinstance(v, dict):
                    res.append(f"Property '{path}{k}' was updated. "
                               f"From [complex value] to '{str(v1)}'")
                elif isinstance(v1, dict):
                    res.append(f"Property '{path}{k}' was updated. "
                               f"From '{str(v)}' to [complex value]")
                else:
                    res.append(f"Property '{path}{k}' was updated. "
                               f"From '{str(v)}' to '{str(v1)}'")
    return new_format("\n".join(res))
