import pytest
from gendiff.diff import generate_diff


@pytest.mark.parametrize(
    'file1,file2,form,expected',
    [('tests/fixtures/files/file1.json', 'tests/fixtures/files/file2.json', "stylish", open('tests/fixtures/files/flat_stylish', "r").read()),
    ('tests/fixtures/files/file1.yml', 'tests/fixtures/files/file2.yml', "stylish", open('tests/fixtures/files/flat_stylish', "r").read()),
    ('tests/fixtures/files/file1.json', 'tests/fixtures/files/file1.yml', "stylish", open('tests/fixtures/files/flat_stylish_1', "r").read()),
    ('tests/fixtures/files/file2.json', 'tests/fixtures/files/file2.yml', "stylish", open('tests/fixtures/files/flat_stylish_2', "r").read()),
    ('tests/fixtures/files/file3.json', 'tests/fixtures/files/file4.yml', "stylish", open('tests/fixtures/files/nested_stylish', "r").read()),
    ('tests/fixtures/files/file3.json', 'tests/fixtures/files/file3.yml', "stylish", open('tests/fixtures/files/nested_stylish_1', "r").read()),
    ('tests/fixtures/files/file4.json', 'tests/fixtures/files/file4.yml', "stylish", open('tests/fixtures/files/nested_stylish_2', "r").read()),
    ('tests/fixtures/files/file1.json', 'tests/fixtures/files/file1.json', "plain", ''),
    ('tests/fixtures/files/file3.json', 'tests/fixtures/files/file4.yml', "plain", open('tests/fixtures/files/nested_plain', "r").read()),
    ('tests/fixtures/files/file3.json', 'tests/fixtures/files/file4.yml', "json", open('tests/fixtures/files/nested_json', "r").read())],
)


def test_generate_diff(file1, file2, form, expected):
    assert generate_diff(file1, file2, form) == expected.rstrip()
