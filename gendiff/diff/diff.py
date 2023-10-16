import json

import yaml
from gendiff.diff.diff_names import (IN_2_FILES, IN_FILE1, IN_FILE2,
                                     DIFF_VALUES, DIFF_TYPES_VALUES)
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


def possible_transform_value(value):
    if isinstance(value, bool):
        file_data = str(value).lower()
    elif value is None:
        file_data = 'null'
    else:
        file_data = value
    return file_data


def transform_filepath(filepath):
    if filepath.endswith('.json'):
        with open(filepath, 'r') as json_file:
            file_data = json.load(json_file)
    else:
        with open(filepath, 'r') as yaml_file:
            file_data = yaml.safe_load(yaml_file)
    return file_data


def check_same_keys(key, data1, data2):
    if data1[key] == data2[key]:
        return [make_diff(data1[key]), IN_2_FILES]
    if isinstance(data1[key], dict) and isinstance(data2[key], dict):
        return [make_diff(data1[key], data2[key]), DIFF_VALUES]
    return [make_diff(data1[key]), make_diff(data2[key]),
            DIFF_TYPES_VALUES]


def make_diff(data1, data2=None):
    if not data2:
        return possible_transform_value(data1)
    data1 = possible_transform_value(data1)
    data2 = possible_transform_value(data2)
    final_diff = {}
    all_files_keys = sorted(list(set(data1) | (set(data2))))
    for key in all_files_keys:
        if key in data1 and key in data2:
            final_diff[key] = check_same_keys(key, data1, data2)
        elif key not in data1 and key in data2:
            final_diff[key] = [make_diff(data2[key]), IN_FILE2]
        elif key not in data2 and key in data1:
            final_diff[key] = [make_diff(data1[key]), IN_FILE1]
    return final_diff


def generate_diff(filepath_1, filepath_2, format='stylish'):
    format_function = get_format_function(format)
    file_1_data = transform_filepath(filepath_1)
    file_2_data = transform_filepath(filepath_2)
    return format_function(make_diff(file_1_data, file_2_data))
