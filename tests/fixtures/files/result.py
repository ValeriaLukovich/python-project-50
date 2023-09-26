import pytest


@pytest.fixture
def test_result():
    return '''{
- follow: False
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True
}'''


@pytest.fixture
def test_compare_file1():
    return '''{
  follow: False
  host: hexlet.io
  proxy: 123.234.53.22
  timeout: 50
}'''


@pytest.fixture
def test_compare_file2():
    return '''{
  host: hexlet.io
  timeout: 20
  verbose: True
}'''


