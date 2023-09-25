import json
from gendiff.generate_diff import generate_diff
from fixtures.files.result import test_result


def test_generate_diff(test_result):
    assert generate_diff("tests/fixtures/files/file1.json", "tests/fixtures/files/file2.json") == test_result
