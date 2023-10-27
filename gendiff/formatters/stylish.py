def to_str(elem):
    if isinstance(elem, bool):
        if elem:
            return "true"
        else:
            return "false"
    elif elem is None:
        return "null"
    return str(elem)


def make_string(elem, d, new_string=''):
    space = d * '    '
    space2 = "\n" + (d + 1) * '    '
    if isinstance(elem, dict):
        for k, v in elem.items():
            if isinstance(v, dict):
                new_string += f"{space2}{str(k)}: {make_string(v, d + 1)}"
            else:
                new_string += f"{space2}{str(k)}: {to_str(v)}"
        return f"{{{new_string}\n{space}}}"
    else:
        return to_str(elem)


def make_stylish(lists, d=1):
    res = []
    for elem in lists:
        k = elem['key']
        v = elem['value']
        v1 = elem['new_value']
        space = d * "    "
        string = space + k
        space2 = (d - 1) * "    "
        string1 = f"{space2}  - {k}: "
        string2 = string1.replace("-", "+")
        match elem['status']:
            case "dict":
                res.append(f"{string}: {make_stylish(v, d + 1)}")
            case "deleted":
                res.append(string1 + make_string(v, d))
            case "added":
                res.append(string2 + make_string(v, d))
            case "updated":
                res.append(string1 + make_string(v, d))
                res.append(string2 + make_string(v1, d))
            case "without changes":
                res.append(f"{string}: {make_string(v, d)}")
            case _:
                raise ValueError
    string = "\n".join(res)
    return f"{{\n{string}\n{(d - 1) * '    '}}}"
