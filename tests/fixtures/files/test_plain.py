import pytest
from gendiff.diff import generate_diff


@pytest.fixture
def result_nested():
    with open('tests/fixtures/files/nested_plain', "r") as read_file:
        return read_file.read()


def test_json_same():
    assert generate_diff('tests/fixtures/files/file1.json', 'tests/fixtures/files/file1.json', "plain") == ''


def test_json(result_nested):
    assert generate_diff('tests/fixtures/files/file3.json', 'tests/fixtures/files/file4.yml', "plain") == result_nested.rstrip()
