def to_str(elem):
    res = str(elem).replace("False", "false")
    return res.replace("True", "true").replace("None", "null")


def make_list(lists):
    new_list = []
    for elem in lists:
        obj = elem['value']
        space = elem['depth'] * "    "
        space1 = (elem['depth'] - 1) * "    " + "  - "
        space2 = (elem['depth'] - 1) * "    " + "  + "
        end = "\n" + space + "}"
        style = space + elem['key']
        style1 = space1 + elem['key']
        style2 = space2 + elem['key']
        if elem['status'] == 'without changes':
            new_list.append(style + ": " + to_str(obj))
        elif elem['status'] == 'deleted':
            new_list.append(style1 + ": " + to_str(obj))
        elif elem['status'] == 'added':
            new_list.append(style2 + ": " + to_str(obj))
        elif elem['status'] == 'dict':
            new_list.append(style + ": {\n" + make_list(obj) + end)
        elif elem['status'] == 'del dict':
            new_list.append(style1 + ": {\n" + make_list(obj) + end)
        elif elem['status'] == 'add dict':
            new_list.append(style2 + ": {\n" + make_list(obj) + end)
    return "\n".join(new_list)


def stylish(lists):
    return "{\n" + make_list(lists) + "\n}"
