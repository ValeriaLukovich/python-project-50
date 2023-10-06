from gendiff.to_string import to_str


def make_list(lists):
    new_list = []
    for elem in lists:
        space = elem['depth'] * "    "
        space1 = (elem['depth'] - 1) * "    " + "  - "
        space2 = (elem['depth'] - 1) * "    " + "  + "
        if elem['status'] == 'without changes':
            new_list.append(space + elem['key'] + ": " + to_str(elem['value']))
        elif elem['status'] == 'deleted':
            new_list.append(space1 + elem['key'] + ": " + to_str(elem['value']))
        elif elem['status'] == 'added':
            new_list.append(space2 + elem['key'] + ": " + to_str(elem['value']))
        elif elem['status'] == 'dict':
            new_list.append(space + elem['key'] + ": {\n" + make_list(elem['value']) + "\n" + space + "}")
        elif elem['status'] == 'deleted dict':
            new_list.append(space1 + elem['key'] + ": {\n" + make_list(elem['value']) + "\n" + space + "}")
        elif elem['status'] == 'added dict':
            new_list.append(space2 + elem['key'] + ": {\n" + make_list(elem['value']) + "\n" + space + "}")
    return "\n".join(new_list)
    
    
def stylish(lists):
    return "{\n" + make_list(lists) + "\n}" 
