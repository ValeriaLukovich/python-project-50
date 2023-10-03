def stylish(lists):
    new_string = ''
    for elem in lists:
        space = elem['depth'] * "    "
        space1 = (elem['depth'] - 1) * "    " + "  - "
        space2 = (elem['depth'] - 1) * "    " + "  + "
        if elem['status'] == 'without changes':
            new_string += space + elem['key'] + ": " + str(elem['value']) + "\n"
        elif elem['status'] == 'deleted':
            new_string += space1 + elem['key'] + ": " + str(elem['value']) + "\n"
        elif elem['status'] == 'added':
            new_string += space2 + elem['key'] + ": " + str(elem['value']) + "\n"
        elif elem['status'] == 'without changes, dict':
            new_string += space + elem['key'] + ":{\n" + str(
            elem['value']) + space + "}\n"
        elif elem['status'] == 'deleted, dict':
            new_string += space1 + elem['key'] + ":{\n " + str(elem['value']) + \
                    space + "}\n"
        elif elem['status'] == 'added, dict':
            new_string += space2 + elem['key'] + ":{\n " + str(elem['value']) + \
                    space + "}\n"

    return new_string.replace("False", "false").replace("True", "true").replace("None", "null")
