from gendiff.parsing_files import parsing_files


def generate_diff(first_file, second_file):
    file1 = parsing_files(first_file)
    file2 = parsing_files(second_file)
    diff = ''
    res = {**file1, **file2}
    for key, value in sorted(res.items()):
        if key in file1 and key in file2 and file1[key] == file2[key]:
            diff += f"  {key}: {value}\n"
        elif key in file1 and key in file2 and file1[key] != file2[key]:
            diff += f"- {key}: {file1[key]}\n"
            diff += f"+ {key}: {file2[key]}\n"
        elif key in file1:
            diff += f"- {key}: {value}\n"
        elif key in file2:
            diff += f"+ {key}: {value}\n"
    return "{\n" + diff + "}"
