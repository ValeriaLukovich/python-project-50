def new_format(string):
    res = string.replace("'False'", "false")
    return res.replace("'True'", "true").replace("'None'", "null")


def check_value(value):
    if isinstance(value, dict):
        value = '[complex value]'
    else:
        value = f"'{str(value)}'"
    return value


def plain(lists, path=''):
    res = []
    for elem in lists:
        k = elem['key']
        v = elem['value']
        v1 = elem['value1']
        string = f"Property '{path}{k}' was"
        if elem['status'] == "dict":
            res.append(plain(v, path + k + '.'))
        else:
            if elem['status'] == "deleted":
                res.append(f"{string} removed")
            elif elem['status'] == "added":
                res.append(f"{string} added with value: {check_value(v)}")
            elif elem['status'] == "updated":
                res.append(f"{string} updated. "
                           f"From {check_value(v)} to {check_value(v1)}")
    return new_format("\n".join(res))
