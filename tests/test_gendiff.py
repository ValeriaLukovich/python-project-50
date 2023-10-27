import pytest
from gendiff.diff import generate_diff


@pytest.mark.parametrize(
    'file1,file2,form,expected',
    [
        ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', "stylish", 'tests/fixtures/flat_stylish'),
        ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', "stylish", 'tests/fixtures/flat_stylish'),
        ('tests/fixtures/file1.json', 'tests/fixtures/file1.yml', "stylish", 'tests/fixtures/flat_stylish_1'),
        ('tests/fixtures/file2.json', 'tests/fixtures/file2.yml', "stylish", 'tests/fixtures/flat_stylish_2'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.yml', "stylish", 'tests/fixtures/nested_stylish'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file3.yml', "stylish", 'tests/fixtures/nested_stylish_1'),
        ('tests/fixtures/file4.json', 'tests/fixtures/file4.yml', "stylish", 'tests/fixtures/nested_stylish_2'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.yml', "plain", 'tests/fixtures/nested_plain'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.yml', "json", 'tests/fixtures/nested_json')],
)
def test_generate_diff(file1, file2, form, expected):
    assert generate_diff(file1, file2, form) == open(expected).read().rstrip()
