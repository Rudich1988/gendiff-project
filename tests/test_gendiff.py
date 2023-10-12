from gendiff import generate_diff

TXT_FILES_DIRECTORY = 'tests/fixtures/txt_files/'


def read_txt_files(paht_file):
    final_string = ''
    with open(paht_file, "r") as input_file:
        for index, line in enumerate(input_file, 1):
            final_string += line
    return final_string


def test_json_files_plain():
    result = generate_diff('file1.json', 'file2.json', format='plain')
    assert result == read_txt_files(TXT_FILES_DIRECTORY + 'files_yaml_plain.txt')


def test_json_files_stylish():
    result = generate_diff('file1.json', 'file2.json', format='stylish')
    assert result == read_txt_files(TXT_FILES_DIRECTORY + 'files_yaml_stylish.txt')


def test_yaml_files_plain():
    result = generate_diff('file1.yaml', 'file2.yaml', format='plain')
    assert result == read_txt_files(TXT_FILES_DIRECTORY + 'files_yaml_plain.txt')


def test_yaml_files_stylish():
    result = generate_diff('file1.yaml', 'file2.yaml', format='stylish')
    assert result == read_txt_files(TXT_FILES_DIRECTORY + 'files_yaml_stylish.txt')


def test_yml_files_stylish():
    result = generate_diff('file1.yml', 'file2.yml', format='stylish')
    assert result == read_txt_files(TXT_FILES_DIRECTORY + 'files_yaml_stylish.txt')


def test_yml_files_plain():
    result = generate_diff('file1.yml', 'file2.yml', format='plain')
    assert result == read_txt_files(TXT_FILES_DIRECTORY + 'files_yaml_plain.txt')


def similar_files_plain():
    result = generate_diff('file1.yml', 'file1.yaml', format='plain')
    assert result == ''


def test_type_plain():
    result = generate_diff('file1.yml', 'file1.yaml', format='plain')
    assert type(result) is str


def test_different_files_types_stylish():
    result = generate_diff('file1.yml', 'file2.json', format='stylish')
    assert result == read_txt_files(TXT_FILES_DIRECTORY + 'files_yaml_stylish.txt')


def test_different_files_format_json():
    result = generate_diff('file1.json', 'file2.json', format='json')
    assert result == read_txt_files(TXT_FILES_DIRECTORY + 'diff_files_json_format.txt')
