import pytest
from gendiff.diff import generate_diff


@pytest.fixture
def result():
    with open('tests/fixtures/files/flat_stylish', "r") as read_file:
        return read_file.read()


@pytest.fixture
def result1():
    with open('tests/fixtures/files/flat_stylish_1', "r") as read_file:
        return read_file.read()


@pytest.fixture
def result2():
    with open('tests/fixtures/files/flat_stylish_2', "r") as read_file:
        return read_file.read()


@pytest.fixture
def result_nested():
    with open('tests/fixtures/files/nested_stylish', "r") as read_file:
        return read_file.read()


@pytest.fixture
def result_nested1():
    with open('tests/fixtures/files/nested_stylish_1', "r") as read_file:
        return read_file.read()


@pytest.fixture
def result_nested2():
    with open('tests/fixtures/files/nested_stylish_2', "r") as read_file:
        return read_file.read()


def test_json(result):
    assert generate_diff('tests/fixtures/files/file1.json', 'tests/fixtures/files/file2.json') == result.rstrip()


def test_yaml(result):
    assert generate_diff('tests/fixtures/files/file1.yml', 'tests/fixtures/files/file2.yml') == result.rstrip()


def test_first_files(result1):
    assert generate_diff('tests/fixtures/files/file1.json', 'tests/fixtures/files/file1.yml') == result1.rstrip()


def test_second_files(result2):
    assert generate_diff('tests/fixtures/files/file2.json', 'tests/fixtures/files/file2.yml') == result2.rstrip()


def test_nested(result_nested):
    assert generate_diff('tests/fixtures/files/file3.json', 'tests/fixtures/files/file4.yml') == result_nested.rstrip()


def test_nested1(result_nested1):
    assert generate_diff('tests/fixtures/files/file3.json', 'tests/fixtures/files/file3.yml') == result_nested1.rstrip()


def test_nested2(result_nested2):
    assert generate_diff('tests/fixtures/files/file4.json', 'tests/fixtures/files/file4.yml') == result_nested2.rstrip()
