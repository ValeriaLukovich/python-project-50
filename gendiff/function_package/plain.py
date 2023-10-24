def check_value(value):
    if isinstance(value, dict):
        value = '[complex value]'
    elif isinstance(value, bool):
        if value:
            value = "true"
        else:
            value = "false"
    elif value is None:
        value = "null"
    else:
        value = f"'{str(value)}'"
    return value


def make_plain(lists, path=''):
    res = []
    for elem in lists:
        k = elem['key']
        v = elem['value']
        v1 = elem['new_value']
        string = f"Property '{path}{k}' was"
        if elem['status'] == "dict":
            res.append(make_plain(v, path + k + '.'))
        else:
            if elem['status'] == "deleted":
                res.append(f"{string} removed")
            elif elem['status'] == "added":
                res.append(f"{string} added with value: {check_value(v)}")
            elif elem['status'] == "updated":
                res.append(f"{string} updated. "
                           f"From {check_value(v)} to {check_value(v1)}")
    return "\n".join(res)
