def to_str(elem):
    res = str(elem).replace("False", "false").replace("True", "true").replace("None", "null")
    return res.replace("True", "true").replace("None", "null")


def make_string(elem, d, new_string=''):
    space = d * '    '
    space2 = (d + 1) * '    '
    if isinstance(elem, dict):
        for k, v in elem.items():
            if isinstance(v, dict):
                new_string += "\n" + space2 + str(k) + ": " + make_string(v, d + 1)
            else:
                new_string += "\n" + space2 + str(k) + ": " + str(v)
        return to_str("{" + new_string + "\n" + space + "}")
    else:
        return to_str(elem)


def make_style(lists, d=1):
    res = []
    for elem in lists:
        space = d * "    "
        space1 = (d - 1) * "    " + "  - "
        space2 = (d - 1) * "    " + "  + "
        k = elem['key']
        v = elem['value']
        v1 = elem['value1']
        if elem['status'] == "dict":
            res.append(space + k + ': {\n' + make_style(v, d + 1) + '\n' + space + '}')
        elif elem['status'] == "deleted":
            res.append(space1 + k + ': ' + make_string(v, d))
        elif elem['status'] == "added":
            res.append(space2 + k + ': ' + make_string(v, d))
        elif elem['status'] == "updated":
            res.append(space1 + k + ': ' + make_string(v, d))
            res.append(space2 + k + ': ' + make_string(v1, d))
        elif elem['status'] == "without changes":
            res.append(space + elem['key'] + ': ' + make_string(v, d))
    return "\n".join(res)


def stylish(lists):
    return "{\n" + make_style(lists) + "\n}"
