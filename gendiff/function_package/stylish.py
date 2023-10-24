def to_str(elem):
    if isinstance(elem, bool):
        if elem:
            elem = "true"
        else:
            elem = "false"
    elif elem is None:
        elem = "null"
    return elem


def make_string(elem, d, new_string=''):
    space = d * '    '
    space2 = "\n" + (d + 1) * '    '
    if isinstance(elem, dict):
        for k, v in elem.items():
            if isinstance(v, dict):
                new_string += space2 + str(k) + ": " + make_string(v, d + 1)
            else:
                new_string += space2 + str(k) + ": " + str(to_str(v))
        return f"{{{new_string}\n{space}}}"
    else:
        return str(to_str(elem))


def make_style(lists, d=1):
    res = []
    for elem in lists:
        k = elem['key']
        v = elem['value']
        v1 = elem['new_value']
        space = d * "    "
        string = space + k
        string1 = (d - 1) * "    " + "  - " + k + ': '
        string2 = string1.replace("-", "+")
        if elem['status'] == "dict":
            res.append(f"{string}: {{\n{make_style(v, d + 1)}\n{space}}}")
        elif elem['status'] == "deleted":
            res.append(string1 + make_string(v, d))
        elif elem['status'] == "added":
            res.append(string2 + make_string(v, d))
        elif elem['status'] == "updated":
            res.append(string1 + make_string(v, d))
            res.append(string2 + make_string(v1, d))
        else:
            elem['status'] == "without changes"
            res.append(f"{string}: {make_string(v, d)}")
    return "\n".join(res)


def make_stylish(lists):
    return f"{{\n{make_style(lists)}\n}}"
