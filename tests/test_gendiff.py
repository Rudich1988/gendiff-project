from gendiff import generate_diff


def test_similar_files():
    result = generate_diff('test_file1.json', 'test_file2.json', files_directory='tests/fixtures/')
    assert result == '{\n  host: hexlet.io\n  timeout: 20\n  verbose: true\n}'


def test_different_files_1():
    result = generate_diff('test_file3.json', 'test_file1.json', files_directory='tests/fixtures/')
    assert result == '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'
