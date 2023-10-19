from gendiff.diff import generate_diff


def test_generate_diff(test_result, test_compare_file1, test_compare_file2, test_compare_nested_files, test_compare_nested_files3, test_compare_nested_files4, test_plain, test_plain1, test_json, test_json1):
    assert generate_diff("tests/fixtures/files/file1.json", "tests/fixtures/files/file2.json", form="stylish") == test_result
    assert generate_diff("tests/fixtures/files/file1.yml", "tests/fixtures/files/file2.yml", form="stylish") == test_result
    assert generate_diff("tests/fixtures/files/file1.json", "tests/fixtures/files/file1.yml", form="stylish") == test_compare_file1
    assert generate_diff("tests/fixtures/files/file2.yml", "tests/fixtures/files/file2.yml", form="stylish") == test_compare_file2
    assert generate_diff("tests/fixtures/files/file3.json", "tests/fixtures/files/file4.json", form="stylish") == test_compare_nested_files
    assert generate_diff("tests/fixtures/files/file3.yml", "tests/fixtures/files/file4.yml", form="stylish") == test_compare_nested_files
    assert generate_diff("tests/fixtures/files/file3.yml", "tests/fixtures/files/file3.json", form="stylish") == test_compare_nested_files3
    assert generate_diff("tests/fixtures/files/file4.yml", "tests/fixtures/files/file4.json", form="stylish") == test_compare_nested_files4
    assert generate_diff("tests/fixtures/files/file3.json", "tests/fixtures/files/file4.json", form="plain") == test_plain
    assert generate_diff("tests/fixtures/files/file3.json", "tests/fixtures/files/file4.json", form="json") == test_json
    assert generate_diff("tests/fixtures/files/file3.json", "tests/fixtures/files/file2.yml", form="json") == test_json1
    assert generate_diff("tests/fixtures/files/file1.json", "tests/fixtures/files/file4.yml", form="plain") == test_plain1
