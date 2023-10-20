import pytest
from gendiff.diff import generate_diff


@pytest.fixture
def result_json():
    with open('tests/fixtures/files/nested_json', "r") as read_file:
        return read_file.read()


def test_nested_json(result_json):
    assert generate_diff('tests/fixtures/files/file3.json', 'tests/fixtures/files/file4.yml', "json") == result_json.rstrip()
