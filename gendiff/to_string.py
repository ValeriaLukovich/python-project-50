def to_str(elem):
    return str(elem).replace("False", "false").replace("True", "true").replace("None", "null")
