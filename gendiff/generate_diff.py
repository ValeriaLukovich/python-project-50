import json


def generate_diff(first_file, second_file):
    file1 = json.load(open(first_file))
    file2 = json.load(open(second_file))
    diff = ''
    for key1, value1 in file1.items():
        for key2, value2 in file2.items():
            if key1 == key2 and value1 == value2:
                diff += f"  {key1}: {value1}\n"
            elif key1 == key2 and value1 != value2:
                diff += f"- {key1}: {value1}\n"
                diff += f"+ {key2}: {value2}\n"
            elif not file2.get(key1):
                string = f"- {key1}: {value1}\n"
                if string not in diff:
                    diff += string
            elif not file1.get(key2):
                string = f"+ {key2}: {value2}\n"
                if string not in diff:
                    diff += string
    return "{\n" + diff + "}"
