from gendiff import generate_diff

TXT_FILES_DIRECTORY = 'tests/fixtures/txt_files/'
CHECKED_FILES_DIRECTORY = 'tests/fixtures/'
FILEPATH1_JSON = CHECKED_FILES_DIRECTORY + 'file1.json'
FILEPATH2_JSON = CHECKED_FILES_DIRECTORY + 'file2.json'
FILEPATH1_YAML = CHECKED_FILES_DIRECTORY + 'file1.yaml'
FILEPATH2_YAML = CHECKED_FILES_DIRECTORY + 'file2.yaml'


def read_txt_files(paht_file):
    final_string = ''
    with open(paht_file, "r") as input_file:
        for index, line in enumerate(input_file, 1):
            final_string += line
    return final_string


def test_json_files_plain():
    result = generate_diff(FILEPATH1_JSON, FILEPATH2_JSON, format='plain')
    assert result == read_txt_files(TXT_FILES_DIRECTORY + 'files_yaml_plain.txt')


def test_json_files_stylish():
    result = generate_diff(FILEPATH1_JSON, FILEPATH2_JSON, format='stylish')
    assert result == read_txt_files(TXT_FILES_DIRECTORY + 'files_yaml_stylish.txt')


def test_yaml_files_plain():
    result = generate_diff(FILEPATH1_YAML, FILEPATH2_YAML, format='plain')
    assert result == read_txt_files(TXT_FILES_DIRECTORY + 'files_yaml_plain.txt')


def test_yaml_files_stylish():
    result = generate_diff(FILEPATH1_YAML, FILEPATH2_YAML, format='stylish')
    assert result == read_txt_files(TXT_FILES_DIRECTORY + 'files_yaml_stylish.txt')


def test_similar_files_plain():
    result = generate_diff(FILEPATH1_JSON, FILEPATH1_YAML, format='plain')
    assert result == ''


def test_type_plain():
    result = generate_diff(FILEPATH1_JSON, FILEPATH1_YAML, format='plain')
    assert type(result) is str


def test_different_files_types_stylish():
    result = generate_diff(FILEPATH1_YAML, FILEPATH2_JSON, format='stylish')
    assert result == read_txt_files(TXT_FILES_DIRECTORY + 'files_yaml_stylish.txt')


def test_different_files_format_json():
    result = generate_diff(FILEPATH1_JSON, FILEPATH2_JSON, format='json')
    assert result == read_txt_files(TXT_FILES_DIRECTORY + 'diff_json_format.txt')
