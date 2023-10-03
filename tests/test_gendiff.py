from gendiff import generate_diff
from gendiff.styles.stylish import stylish


def test_similar_files():
    result = generate_diff('test_file1.json', 'test_file2.json', format=stylish, files_directory='tests/fixtures/')
    assert result == '{\n    host: hexlet.io\n    timeout: 20\n    verbose: true\n}'


def test_different_files_1():
    result = generate_diff('test_file3.json', 'test_file1.json', format=stylish, files_directory='tests/fixtures/')
    assert result == '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'


def test_type_result():
    result = generate_diff('test_file3.json', 'test_file1.json', format=stylish, files_directory='tests/fixtures/')
    assert type(result) == str


def test_different_json_yml_files():
    result = generate_diff('test_file3.json', 'test_file1.yml', format=stylish, files_directory='tests/fixtures/')
    assert result == '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'


def test_similar_json_yml_files():
    result = generate_diff('test_file1.yml', 'test_file2.json', format=stylish, files_directory='tests/fixtures/')
    assert result == '{\n    host: hexlet.io\n    timeout: 20\n    verbose: true\n}'


def test_similar_json_yml_files():
    result = generate_diff('test_file1.yaml', 'test_file2.json', format=stylish, files_directory='tests/fixtures/')
    assert result == '{\n    host: hexlet.io\n    timeout: 20\n    verbose: true\n}'


def test_different_yml_files():
    result = generate_diff('test_file2.yml', 'test_file1.yml', format=stylish, files_directory='tests/fixtures/')
    assert result == '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'


def test_different_yaml_files():
    result = generate_diff('test_file2.yaml', 'test_file1.yaml', format=stylish, files_directory='tests/fixtures/')
    assert result == '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'


def test_different_yml_yaml_files():
    result = generate_diff('test_file2.yml', 'test_file1.yaml', format=stylish, files_directory='tests/fixtures/')
    assert result == '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'


def test_similar_yml_yaml_files():
    result = generate_diff('test_file1.yaml', 'test_file1.yml', format=stylish, files_directory='tests/fixtures/')
    assert result == '{\n    host: hexlet.io\n    timeout: 20\n    verbose: true\n}'


def test_different_yaml_nesting_files():
    result = generate_diff('file_with_nesting1.yaml', 'file_with_nesting2.yaml', format=stylish, files_directory='tests/fixtures/')
    assert result == "{\n    dictionary_1: {\n        a: 1\n        b: 2\n    }\n    dictionary_2: {\n        c: 3\n        d: 4\n    }\n  - dictionary_3: {\n        bool: False\n    }\n  + dictionary_4: {\n        bool: {\n            false: True\n        }\n    }\n    number: 2\n}"
