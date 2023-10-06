from gendiff.generate_diff import generate_diff
from tests.fixtures.files.result import test_result, test_compare_file1, test_compare_file2, test_compare_nested_files, test_compare_nested_files3, test_compare_nested_files4
import pytest


@pytest.mark.parametrize("file1", ["tests/fixtures/files/file1.json", "tests/fixtures/files/file2.json"])
@pytest.mark.parametrize("file2", ["tests/fixtures/files/file1.yml", "tests/fixtures/files/file2.yml"])
@pytest.mark.parametrize("file3", ["tests/fixtures/files/file3.json", "tests/fixtures/files/file4.json"])
@pytest.mark.parametrize("file4", ["tests/fixtures/files/file3.yml", "tests/fixtures/files/file4.yml"])
def test_generate_diff(file1, file2, file3, file4, test_result, test_compare_file1, test_compare_file2, test_compare_nested_files, test_compare_nested_files3, test_compare_nested_files4):
    assert generate_diff("tests/fixtures/files/file1.json", "tests/fixtures/files/file2.json") == test_result
    assert generate_diff("tests/fixtures/files/file1.yml", "tests/fixtures/files/file2.yml") == test_result
    assert generate_diff("tests/fixtures/files/file1.json", "tests/fixtures/files/file1.yml") == test_compare_file1
    assert generate_diff("tests/fixtures/files/file2.yml", "tests/fixtures/files/file2.yml") == test_compare_file2
    assert generate_diff("tests/fixtures/files/file3.json", "tests/fixtures/files/file4.json") == test_compare_nested_files
    assert generate_diff("tests/fixtures/files/file3.yml", "tests/fixtures/files/file4.yml") == test_compare_nested_files
    assert generate_diff("tests/fixtures/files/file3.yml", "tests/fixtures/files/file3.json") == test_compare_nested_files3
    assert generate_diff("tests/fixtures/files/file4.yml", "tests/fixtures/files/file4.json") == test_compare_nested_files4
