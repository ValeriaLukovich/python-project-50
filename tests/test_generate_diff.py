from gendiff.diff import generate_diff
from gendiff.function_package.plain import plain
from gendiff.function_package.stylish import stylish
from gendiff.function_package.json import json_f
from tests.conftest import test_result, test_compare_file1, test_compare_file2, test_compare_nested_files, test_compare_nested_files3, test_compare_nested_files4, test_plain, test_plain1, test_json, test_json1
import pytest


def test_generate_diff(test_result, test_compare_file1, test_compare_file2, test_compare_nested_files, test_compare_nested_files3, test_compare_nested_files4, test_plain, test_plain1, test_json, test_json1):
    assert generate_diff("tests/fixtures/files/file1.json", "tests/fixtures/files/file2.json", format=stylish) == test_result
    assert generate_diff("tests/fixtures/files/file1.yml", "tests/fixtures/files/file2.yml", format=stylish) == test_result
    assert generate_diff("tests/fixtures/files/file1.json", "tests/fixtures/files/file1.yml", format=stylish) == test_compare_file1
    assert generate_diff("tests/fixtures/files/file2.yml", "tests/fixtures/files/file2.yml", format=stylish) == test_compare_file2
    assert generate_diff("tests/fixtures/files/file3.json", "tests/fixtures/files/file4.json", format=stylish) == test_compare_nested_files
    assert generate_diff("tests/fixtures/files/file3.yml", "tests/fixtures/files/file4.yml", format=stylish) == test_compare_nested_files
    assert generate_diff("tests/fixtures/files/file3.yml", "tests/fixtures/files/file3.json", format=stylish) == test_compare_nested_files3
    assert generate_diff("tests/fixtures/files/file4.yml", "tests/fixtures/files/file4.json", format=stylish) == test_compare_nested_files4
    assert generate_diff("tests/fixtures/files/file3.json", "tests/fixtures/files/file4.json", format=plain) == test_plain
    assert generate_diff("tests/fixtures/files/file3.json", "tests/fixtures/files/file4.json", format=json_f) == test_json
    assert generate_diff("tests/fixtures/files/file3.json", "tests/fixtures/files/file2.yml", format=json_f) == test_json1
    assert generate_diff("tests/fixtures/files/file1.json", "tests/fixtures/files/file4.yml", format=plain) == test_plain1
