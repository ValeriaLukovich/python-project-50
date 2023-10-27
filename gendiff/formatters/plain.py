def check_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        if value:
            return "true"
        else:
            return "false"
    elif value is None:
        return "null"
    elif isinstance(value, int):
        return value
    return f"'{value}'"


def make_plain(lists, path=''):
    res = []
    for elem in lists:
        k = elem['key']
        v = elem['value']
        v1 = elem['new_value']
        string = f"Property '{path}{k}' was"
        match elem['status']:
            case "dict":
                res.append(make_plain(v, f"{path}{k}."))
            case "deleted":
                res.append(f"{string} removed")
            case "added":
                res.append(f"{string} added with value: {check_value(v)}")
            case "updated":
                res.append(f"{string} updated. "
                           f"From {check_value(v)} to {check_value(v1)}")
            case "without changes":
                continue
            case _:
                raise ValueError
    return "\n".join(res)
