import pytest
from gendiff.diff import generate_diff


@pytest.mark.parametrize(
    'file1,file2,form,expected',
    [
        ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', "stylish", open('tests/fixtures/flat_stylish', "r").read()),
        ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', "stylish", open('tests/fixtures/flat_stylish', "r").read()),
        ('tests/fixtures/file1.json', 'tests/fixtures/file1.yml', "stylish", open('tests/fixtures/flat_stylish_1', "r").read()),
        ('tests/fixtures/file2.json', 'tests/fixtures/file2.yml', "stylish", open('tests/fixtures/flat_stylish_2', "r").read()),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.yml', "stylish", open('tests/fixtures/nested_stylish', "r").read()),
        ('tests/fixtures/file3.json', 'tests/fixtures/file3.yml', "stylish", open('tests/fixtures/nested_stylish_1', "r").read()),
        ('tests/fixtures/file4.json', 'tests/fixtures/file4.yml', "stylish", open('tests/fixtures/nested_stylish_2', "r").read()),
        ('tests/fixtures/file1.json', 'tests/fixtures/file1.json', "plain", ''),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.yml', "plain", open('tests/fixtures/nested_plain', "r").read()),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.yml', "json", open('tests/fixtures/nested_json', "r").read())],
)
def test_generate_diff(file1, file2, form, expected):
    assert generate_diff(file1, file2, form) == expected.rstrip()
