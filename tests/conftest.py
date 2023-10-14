import pytest


@pytest.fixture
def test_result():
    return '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


@pytest.fixture
def test_compare_file1():
    return '''{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''


@pytest.fixture
def test_compare_file2():
    return '''{
    host: hexlet.io
    timeout: 20
    verbose: true
}'''


@pytest.fixture
def test_compare_nested_files():
    return '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''


@pytest.fixture
def test_compare_nested_files3():
    return '''{
    common: {
        setting1: Value 1
        setting2: 200
        setting3: true
        setting6: {
            doge: {
                wow: 
            }
            key: value
        }
    }
    group1: {
        baz: bas
        foo: bar
        nest: {
            key: value
        }
    }
    group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
}'''


@pytest.fixture
def test_compare_nested_files4():
    return '''{
    common: {
        follow: false
        setting1: Value 1
        setting3: null
        setting4: blah blah
        setting5: {
            key5: value5
        }
        setting6: {
            doge: {
                wow: so much
            }
            key: value
            ops: vops
        }
    }
    group1: {
        baz: bars
        foo: bar
        nest: str
    }
    group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''


@pytest.fixture
def test_plain():
    return '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''


@pytest.fixture
def test_plain1():
    return '''Property 'common' was added with value: [complex value]
Property 'follow' was removed
Property 'group1' was added with value: [complex value]
Property 'group3' was added with value: [complex value]
Property 'host' was removed
Property 'proxy' was removed
Property 'timeout' was removed'''


@pytest.fixture
def test_json():
    return '''[{"status": "dict", "depth": 1, "key": "common", "value": [{"status": "added", "depth": 2, "key": "follow", "value": false, "value1": 0}, {"status": "without changes", "depth": 2, "key": "setting1", "value": "Value 1", "value1": 0}, {"status": "deleted", "depth": 2, "key": "setting2", "value": 200, "value1": 0}, {"status": "updated", "depth": 2, "key": "setting3", "value": true, "value1": null}, {"status": "added", "depth": 2, "key": "setting4", "value": "blah blah", "value1": 0}, {"status": "added", "depth": 2, "key": "setting5", "value": {"key5": "value5"}, "value1": 0}, {"status": "dict", "depth": 2, "key": "setting6", "value": [{"status": "dict", "depth": 3, "key": "doge", "value": [{"status": "updated", "depth": 4, "key": "wow", "value": "", "value1": "so much"}], "value1": 0}, {"status": "without changes", "depth": 3, "key": "key", "value": "value", "value1": 0}, {"status": "added", "depth": 3, "key": "ops", "value": "vops", "value1": 0}], "value1": 0}], "value1": 0}, {"status": "dict", "depth": 1, "key": "group1", "value": [{"status": "updated", "depth": 2, "key": "baz", "value": "bas", "value1": "bars"}, {"status": "without changes", "depth": 2, "key": "foo", "value": "bar", "value1": 0}, {"status": "updated", "depth": 2, "key": "nest", "value": {"key": "value"}, "value1": "str"}], "value1": 0}, {"status": "deleted", "depth": 1, "key": "group2", "value": {"abc": 12345, "deep": {"id": 45}}, "value1": 0}, {"status": "added", "depth": 1, "key": "group3", "value": {"deep": {"id": {"number": 45}}, "fee": 100500}, "value1": 0}]'''


@pytest.fixture
def test_json1():
    return '''[{"status": "deleted", "depth": 1, "key": "common", "value": {"setting1": "Value 1", "setting2": 200, "setting3": true, "setting6": {"key": "value", "doge": {"wow": ""}}}, "value1": 0}, {"status": "deleted", "depth": 1, "key": "group1", "value": {"baz": "bas", "foo": "bar", "nest": {"key": "value"}}, "value1": 0}, {"status": "deleted", "depth": 1, "key": "group2", "value": {"abc": 12345, "deep": {"id": 45}}, "value1": 0}, {"status": "added", "depth": 1, "key": "host", "value": "hexlet.io", "value1": 0}, {"status": "added", "depth": 1, "key": "timeout", "value": 20, "value1": 0}, {"status": "added", "depth": 1, "key": "verbose", "value": true, "value1": 0}]'''
