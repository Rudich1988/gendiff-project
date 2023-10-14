import json

import yaml
from gendiff.styles.json_style import get_json_style
from gendiff.styles.plain import get_plain_style
from gendiff.styles.stylish import get_stylish


def get_format_function(format_name):
    match format_name:
        case 'stylish':
            return get_stylish
        case 'plain':
            return get_plain_style
        case 'json':
            return get_json_style


def check_value(value):
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    else:
        if isinstance(value, bool):
            file_data = str(value).lower()
        elif value is None:
            file_data = 'null'
        else:
            file_data = value
        return file_data


def create_file_path(filepath, directory='tests/fixtures/'):
    if '/' in filepath:
        return filepath
    return directory + filepath


def processing_file_path(filepath):
    if filepath[-5:] == '.json':
        filepath = create_file_path(filepath)
        file_data = json.load(open(filepath))
    elif filepath[-5:] == '.yaml' or filepath[-4:] == '.yml':
        filepath = create_file_path(filepath)
        with open(filepath, 'r') as yaml_file:
            file_data = yaml.safe_load(yaml_file)
    return file_data


def transform_file(filepath):
    if filepath[-5:] == '.json':
        filepath = create_file_path(filepath)
        file_data = json.load(open(filepath))
    else:
        filepath = create_file_path(filepath)
        with open(filepath, 'r') as yaml_file:
            file_data = yaml.safe_load(yaml_file)
    return file_data


def check_same_keys(key, data1, data2):
    if data1[key] == data2[key]:
        return (make_diff(data1[key]), 'in 2 files')
    else:
        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            return (make_diff(data1[key], data2[key]), 'diff values')
        else:
            return (make_diff(data1[key]), make_diff(data2[key]),
                    'diff types values')


def make_diff(data1, data2=None):
    if not isinstance(data1, dict) or data2 is None:
        return check_value(data1)
    data1 = check_value(data1)
    data2 = check_value(data2)
    final_diff = {}
    all_files_keys = sorted(list(set(data1) | (set(data2))))
    for key in all_files_keys:
        if key in data1 and key in data2:
            final_diff[key] = check_same_keys(key, data1, data2)
        elif key not in data1 and key in data2:
            final_diff[key] = (make_diff(data2[key]), 'in file2')
        elif key not in data2 and key in data1:
            final_diff[key] = (make_diff(data1[key]), 'in file1')
    return final_diff


def generate_diff(filepath_1, filepath_2, format='stylish'):
    format_function = get_format_function(format)
    file_1_data = processing_file_path(filepath_1)
    file_2_data = processing_file_path(filepath_2)
    return format_function(make_diff(file_1_data, file_2_data))
